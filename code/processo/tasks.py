from celery import shared_task
from .scraping.tribunais.tj_rj import TjRjScraping
from processo.models import ProcessosMovimento, Processos
import logging
from django.conf import settings

logger = logging.getLogger("processo")


@shared_task
def track_new_process(lawsuit_number: str, lawsuit_pk: int):
    indetifier_number = lawsuit_number[16:20]
    lawsuit = Processos.objects.get(id=lawsuit_pk)
    if indetifier_number in settings.TRACKED:
        try:
            tj_rj = TjRjScraping(lawsuit.codigo_processo)
            data = tj_rj.last_process_moviment()
            if data:
                data_str = ""
                for string in data["data"]:
                    data_str += f"{string}\n"

                if lawsuit.track_history.count() != 0:
                    if data["date"] != lawsuit.track_history.first().last_date:
                        logger.warning(
                            f"{lawsuit.track_history.first().last_date} != {str(data['date'] + 'DIFF')}"
                        )

                ProcessosMovimento.objects.create(
                    processo_id=lawsuit.pk,
                    tipo_movimento=data["movimento"],
                    last_date=data["date"],
                    data=data_str
                )
        except Exception as e:
            logger.error(
                f"Error - {e} - cant possible track {lawsuit_number}"
            )
    else:
        logger.info("That process cant be tracked")


@shared_task
def search_new_lawsuits_changes():
    from django.conf import settings
    for tracked_number in settings.TRACKED:
        lawsuits = Processos.objects.filter(
            codigo_processo__icontains=tracked_number
        )
        for lawsuit in lawsuits:
            if lawsuit.track_history.count() < 5:
                track_new_process(lawsuit.codigo_processo, lawsuit.pk)
            else:
                lawsuit.track_history.last().delete()
                track_new_process(lawsuit.codigo_processo, lawsuit.pk)

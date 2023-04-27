from celery import shared_task
from .scraping.tribunais.tj_rj import TjRjScraping
from processo.models import ProcessosMovimento, Processos
import logging
from django.conf import settings

logger = logging.getLogger("processo")


@shared_task
def track_new_process(numero_processo, id):
    indetifier_number = numero_processo[:15] + numero_processo[21:]
    if indetifier_number in settings.TRACKED:
        try:
            tj_rj = TjRjScraping(numero_processo)
            data = tj_rj.last_process_moviment()
            data_str = ""
            for string in data["data"]:
                data_str += f"{string}\n"
            ProcessosMovimento.objects.create(
                processo_id=id,
                tipo_movimento=data["movimento"],
                last_date=data["date"],
                data=data_str
            )
        except Exception as e:
            logger.error(
                f"Error - {e} - cant possible track {numero_processo}"
            )
    else:
        logger.info("That process cant be traceable")


@shared_task
def search_process_changes():
    for process in Processos.objects.all():
        if process.tracked:
            process_moviments = ProcessosMovimento.objects.filter(
                processo=process
            ).order_by("-id")
            if process_moviments:
                tj_rj = TjRjScraping(process.codigo_processo)
                try:
                    data = tj_rj.last_process_moviment()
                except Exception as e:
                    logger.error(
                        f"Error - {e} - {process.codigo_processo}"
                    )
                    continue

                data_str = ""
                for string in data["data"]:
                    data_str += f"{string}\n"

                if data_str != process_moviments.first().data:
                    if len(process_moviments) == 5:
                        process_moviments.last().delete()
                    track_new_process(process.codigo_processo, process.pk)
            else:
                track_new_process(process.codigo_processo, process.pk)

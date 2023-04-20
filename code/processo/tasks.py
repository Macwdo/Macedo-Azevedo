from celery import shared_task
from .scraping.tribunais.tj_rj import TjRjScraping
from processo.models import ProcessosMovimento, Processos
import logging
from datetime import date


@shared_task
def track_new_process(numero_processo, id):
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
        logging.error(f"Error ao monitorar o novo processo {numero_processo}")


@shared_task
def search_process_alterations():
    for process in Processos.objects.all():
        if process.tracked:
            last_process_moviment = ProcessosMovimento.objects.filter(
                processo=process
            ).order_by("-id")
            if last_process_moviment:
                tj_rj = TjRjScraping(process.codigo_processo)
                try:
                    data = tj_rj.last_process_moviment()
                except Exception as e:
                    logging.warning(
                        f"Error TJ-RJ - {process.codigo_processo} - {date.today()} - {e} "
                    )
                    continue

                data_str = ""
                for string in data["data"]:
                    data_str += f"{string}\n"

                if data_str != last_process_moviment.first().data:
                    process_moviments = ProcessosMovimento.objects.filter(
                        processo=process
                    )
                    if len(process_moviments) == 5:
                        process_moviments.last().delete()
                    track_new_process(process.codigo_processo, process.pk)
            else:
                track_new_process(process.codigo_processo, process.pk)

    return "success"

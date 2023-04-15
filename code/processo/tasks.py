from celery import shared_task
from .scraping.tribunais.tj_rj import TjRjScraping
from .models import ProcessoMovimento

@shared_task
def track_process(numero_processo, id):
    try:
        tj_rj = TjRjScraping(numero_processo)
        data = tj_rj.history_process()
        data_str = ""
        for string in data["data"]:
            data_str += f"{string}\n"
        processo_movimento = ProcessoMovimento.objects.create(
            processo_id=id,
            tipo_movimento=data["movimento"],
            last_date=data["date"],
            data=data_str
        )
    except:
        raise Exception()
from celery import shared_task
from time import sleep
from .scraping.tribunais.tj_rj import TjRjScraping

@shared_task
def get_last_change_process():
    tj_rj = TjRjScraping("0030307-60.2022.8.19.0001")
    data = tj_rj.run()
    return data
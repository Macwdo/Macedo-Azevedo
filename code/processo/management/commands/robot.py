from django.core.management.base import BaseCommand
from processo.scraping.tribunais.tj_rj import TjRjScraping


class Command(BaseCommand):
    def handle(self, *args, **options):
        processos_ws = TjRjScraping("0030307-60.2022.8.19.0001")
        data = processos_ws.run()
        print(data)



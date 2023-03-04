from datetime import datetime

from pytz import timezone


def get_current_time():
    return datetime.now(tz=timezone('America/Sao_Paulo'))


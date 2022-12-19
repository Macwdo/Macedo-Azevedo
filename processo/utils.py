import datetime
import pytz


timezone = pytz.timezone('America/Sao_Paulo')

def get_current_time(timezone=timezone):
    return datetime.datetime.now(tz=timezone)



"""Marcar um evento em um tempo específico."""
import sched
import time
from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)


def reschedule():
    """Zere os segundos de now e some mais 1 minuto."""
    new_target = datetime.now().replace(second=0, microsecond=0)
    new_target += timedelta(minutes=1)
    print(new_target)

    scheduler.enterabs(new_target.timestamp(),
                       priority=100,
                       action=google_request)

    # scheduler.enterabs(datetime(2018, 5, 14, 22, 57).timestamp(),
    #                    priority=100,
    #                    action=saytime)


def saytime():
    print(time.ctime())
    reschedule()


def google_request():
    from requests import get
    get('http://google.com').status_code
    reschedule()


reschedule()

scheduler.run(blocking=False)

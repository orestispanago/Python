''' Tests function of "APScheduler" library'''

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone

launch_datetime = '2018-02-09 20:42:00'

def greet():
    timestamp = datetime.now(timezone.utc)
    now= timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now,'hello')
    return
try:
    sched = BlockingScheduler(standalone=True)
    sched.add_job(greet, 'interval', seconds=1, start_date = launch_datetime)
    sched.start()
except (KeyboardInterrupt):
    sched.shutdown(wait=False)
    print('Exiting nicely...')

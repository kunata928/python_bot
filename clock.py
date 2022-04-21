from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import main


sched = BlockingScheduler()
now = datetime.now()
delta_time = datetime.now() + timedelta(minutes=2)
# scheduler.add_job(send_message_to_admin, "date", run_date=datetime(2022, 1, 8, 18, 50), args=(bot,))
# @sched.add_job(send_remind.main(), trigger=, args=None, )

print("now time: ", datetime.now().time().hour, ":", datetime.now().time().minute)
print("delta time: ", delta_time.time().hour, ":", delta_time.time().minute)


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    time_now = datetime.now().time()
    # next_time_remind =
    if delta_time.time().hour == time_now.hour and delta_time.time().minute == time_now.minute:
        main.bot.send_message(main.MY_ID_CHAT, text="it work????")
        print('This job is run')


sched.start()


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import psycopg2
import main
import settings as stg

db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
db_object = db_connection.cursor()
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    now_dt = datetime.now()
    db_object.execute(f"SELECT user_id, text "
                      f"FROM reminds "
                      f"WHERE time = '{now_dt.time().replace(second=0, microsecond=0)}' AND date = '{now_dt.date()}'")
    result = db_object.fetchall()
    if result:
        for res in result:
            main.bot.send_message(res[0], text=res[1])


sched.start()

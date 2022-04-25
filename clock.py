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
    print(result)
    if result:
        # here must be for loop for all of founded reminds!!!!!!!!!!!!!!!!!!!!!!
        main.bot.send_message(result[0][0], text=result[0][1])
        print('This job is run')


sched.start()


# -----------add new remind ro table--------- start
# now = datetime.now()
# delta_time = now + timedelta(minutes=2)

# db_object.execute(f"SELECT count(id) "
#                   f"FROM reminds ")
# id = int(db_object.fetchone()[0]) + 1
# user_id = main.MY_ID_CHAT
# time = delta_time.time().replace(second=0, microsecond=0)
# date = delta_time.date()
# text = "it work????"
# db_object.execute("INSERT INTO reminds(id, user_id, time, date, text) VALUES (%s, %s, %s, %s, %s)", (id, user_id, time, date, text))
# db_connection.commit()
# -----------add new remind ro table--------- end

# now_dt = datetime.now()
# db_object.execute(f"SELECT user_id, text "
#                   f"FROM reminds "
#                   f"WHERE time = '{now_dt.time().replace(second=0, microsecond=0)}' AND date = '{now_dt.date()}'")
# result = db_object.fetchall()
# print(result)
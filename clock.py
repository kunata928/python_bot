from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime, timezone, timedelta
import psycopg2
from psycopg2 import Error
import main
import settings as stg

db_connection = 0
LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

try:
    sched = BlockingScheduler()

    db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
    db_object = db_connection.cursor()

    @sched.scheduled_job('interval', minutes=1)
    def timed_job():

        now_dt = datetime.now() - timedelta(hours=int(str(stg.LOCAL_TIMEZONE)))
        print(now_dt.time().replace(second=0, microsecond=0))
        db_object.execute(f"SELECT user_id, text, id "
                          f"FROM reminds "
                          f"WHERE time = '{now_dt.time().replace(second=0, microsecond=0)}' AND date = '{now_dt.date()}'")
        result = db_object.fetchall()
        if result:
            for res in result:
                main.bot.send_message(res[0], text=res[1])
                sql_delete_query = """DELETE FROM reminds WHERE id = %s"""
                db_object.execute(sql_delete_query, (res[2],))
            db_connection.commit()

    sched.start()

except (Exception, Error) as error:
    print("Error while working with PostgreSQL", error)

except KeyboardInterrupt:
    print("cleanup")
    if db_connection:
        db_object.close()
        db_connection.close()
        print("Connection with PostgreSQL closed")
finally:
    print("cleanup")
    if db_connection:
        db_object.close()
        db_connection.close()
        print("Connection with PostgreSQL closed")

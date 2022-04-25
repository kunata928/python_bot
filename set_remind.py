import psycopg2
import settings as stg
MY_ID_CHAT = 273224124


db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
db_object = db_connection.cursor()


def set_remind_job(data):
    db_object.execute(f"SELECT count(id) "
                      f"FROM reminds ")
    id_table = int(db_object.fetchone()[0]) + 1
    time = data['time_date'].time().replace(second=0, microsecond=0)
    date = data['time_date'].date()
    db_object.execute("INSERT INTO reminds(id, user_id, time, date, text) VALUES (%s, %s, %s, %s, %s)",
                      (id_table, data['user_id'], time, date, data['text']))
    db_connection.commit()
    print('set job')

import psycopg2
from psycopg2 import Error
from datetime import datetime, timezone, timedelta
import settings as stg
import parser_message


def set_remind_job(data):
    id_table = 0
    db_connection = 0
    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()
        db_object.execute(f"SELECT nextval('serialIDS');")
        id_table = db_object.fetchone()[0]
        if data['type'] == 'at':
            db_object.execute(f"SELECT tz FROM users WHERE id = {data['user_id']}")
            res = db_object.fetchone()
            delta = timedelta(hours=res[0]) if res else timedelta(hours=int(stg.DEFAULT_TIMEZONE))
        else:
            delta = timedelta(hours=int(str(stg.LOCAL_TIMEZONE)))
        data['time_date'] = data['time_date'] - delta
        time = data['time_date'].time().replace(second=0, microsecond=0)
        date = data['time_date'].date()
        db_object.execute("INSERT INTO reminds(id, user_id, time, date, text) VALUES (%s, %s, %s, %s, %s)",
                          (id_table, data['user_id'], time, date, data['text']))
        db_connection.commit()
    except (Exception, Error) as error:
        id_table = 0
        print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")
    return id_table


def message_processing(message): #after user input remind check if valid - add remind; else give notification
    data = parser_message.parse_message(message.text)
    if not data:
        text = 'If you want to add a remind, type message like: '"<After> <time> <msg> " \
             "After 5 h/min remind to drink water"
    else:
        data['user_id'] = message.from_user.id
        remind_id = set_remind_job(data)
        text = "Set remind with id " + str(remind_id)
    return text


def count_reminds_for_user(user_id): #to count reminds for user to check limit
    db_connection = 0
    result = -1
    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()
        db_object.execute(f"SELECT count(id) "
                          f"FROM reminds "
                          f"WHERE user_id = {user_id}")
        result = int(db_object.fetchone()[0])
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")
    return result
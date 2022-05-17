import psycopg2
from psycopg2 import Error
import settings as stg


def show_user_tz(user_id):
    db_connection = 0
    result = 0
    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()
        db_object.execute(f"SELECT tz "
                          f"FROM users "
                          f"WHERE id = {user_id}")
        res = db_object.fetchone()
        if res:
            result = int(res[0])
        else:
            result = stg.DEFAULT_TIMEZONE
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")
    return result


def set_tz_DB(user_id, tz):
    db_connection = 0
    text_message = "Incorrect timezone. Try again (for example <+3> or <-11>)"
    try:
        int_tz = int(tz)
    except:
        return text_message

    if int_tz > 12 or int_tz < -12:
        return text_message

    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()
        db_object.execute(f"SELECT id "
                          f"FROM users "
                          f"WHERE id = {user_id}")
        result = db_object.fetchone()
        if result:
            db_object.execute(f"UPDATE users "
                              f"SET tz = {int_tz} "
                              f"WHERE id = {user_id}")
        else:
            db_object.execute(f"INSERT "
                              f"INTO users(id, tz) "
                              f"VALUES (%s, %s)",
                              (user_id, int_tz))
        db_connection.commit()
        sign = '+' if int_tz >= 0 else ''
        text_message = f"Successfully! Now your timezone is UTC {sign}{str(int_tz)}"
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")
    return text_message

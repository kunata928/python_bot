import psycopg2
from psycopg2 import Error
import settings as stg


def list_users_reminds(user_id):
    list_reminds = ""
    db_connection = 0
    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()

        db_object.execute(f"SELECT id, text  "
                          f"FROM reminds "
                          f"WHERE user_id = {user_id}")
        result = db_object.fetchall()
        if result:
            list_reminds += "You have follow active reminds:\n"
            for res in result:
                list_reminds += str(res[0]) + " -> " + res[1] + "\n"
        else:
            list_reminds += "You have follow active reminds:\n"
    except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")
    return list_reminds


def remove_remind(id_remind):
    db_connection = 0
    code = 0
    try:
        db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
        db_object = db_connection.cursor()
        db_object.execute(f"DELETE "
                          f"FROM reminds "
                          f"WHERE id = {id_remind}")
        db_connection.commit()
        code = 1
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if db_connection:
            db_object.close()
            db_connection.close()
            print("Connection with PostgreSQL closed")
    return code

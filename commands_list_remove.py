import psycopg2
import settings as stg
MY_ID_CHAT = 273224124


db_connection = psycopg2.connect(stg.DB_URI, sslmode="require")
db_object = db_connection.cursor()


def list_users_reminds(user_id):
    list_reminds = ""
    db_object.execute(f"SELECT id, text  "
                      f"FROM reminds "
                      f"WHERE user_id = {user_id}")
    result = db_object.fetchall()
    if result:
        list_reminds += "You have follow active reminds:\n"
        for res in result:
            list_reminds += str(res[0]) + " -> " + res[1] + "\n"
    return list_reminds

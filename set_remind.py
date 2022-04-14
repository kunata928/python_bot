# here must be DB with jobs
# from datetime import datetime
MY_ID_CHAT = 273224124


def send(bot, data):
    # bot.send_message(data['user_id'], text=data['text'])
    # bot.send_message(MY_ID_CHAT, text="ok")
    print('ok')


def set_remind_job(data, bot, sched):
    print('set job')
    sched.add_job(send, "date", run_date=data['time_date'], args=(bot, data,), timezone='Europe/Moscow') #datetime(2022, 1, 8, 18, 50)
    # sched.add_job(print, "date", run_date=datetime(2022, 4, 13, 14, 51), args="okkkkk", timezone='Europe/Moscow') #datetime(2022, 1, 8, 18, 50)
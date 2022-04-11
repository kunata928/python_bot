# here must be DB with jobs
def set_remind_job(data, bot, sched):
    sched.add_job(bot.send_message(data['user_id'], text=data['text']),
                  "date", run_date=data['time_date'], args=(bot,)) #datetime(2022, 1, 8, 18, 50)
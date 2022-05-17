from datetime import datetime, timezone, timedelta


# MY_ID_CHAT = 273224124

LOCAL_TIMEZONE = "-04"#datetime.now(timezone.utc).astimezone().tzinfo
local_timezone = datetime.utcnow().time()

tz_user = -3
date_time = datetime(hour=(23 - tz_user) % 24, minute=00, year=2022, month=6, day=14)
print(date_time)

from datetime import datetime, timezone, timedelta


# MY_ID_CHAT = 273224124

LOCAL_TIMEZONE = "-04"#datetime.now(timezone.utc).astimezone().tzinfo
local_timezone = datetime.utcnow().time()

print(local_timezone)

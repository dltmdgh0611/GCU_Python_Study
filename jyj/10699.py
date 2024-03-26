import datetime as dt
birthdate = dt.datetime.now(dt.timezone.utc)
print(birthdate.astimezone().strftime("%Y-%m-%d"))
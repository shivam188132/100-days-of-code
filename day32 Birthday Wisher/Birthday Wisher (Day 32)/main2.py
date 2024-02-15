import datetime as dt
now = dt.datetime.now()
print(now)
print(type(now))
month = now.month
print(month)
day_of_week = now.weekday()
print(type(day_of_week))
# as python counts from 0
print(day_of_week+1)
print(now.time())

date_of_birth = dt.datetime(year=2003, month=2, day=7, hour=12, minute=23)
print(date_of_birth)
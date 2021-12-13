import datetime
import pytz
from dateutil.relativedelta import relativedelta

#now = datetime.datetime.now()
#timezone = pytz.timezone("Europe/Moscow")
#print(f'now: {now}')
#print(f'type of now: {type(now)}')
#print(f'timezone: {timezone}')
#print(f'type of timezone: {type(timezone)}')

#now_with_tz = timezone.localize(now)
#print(f'now_with_tz: {now_with_tz}')
#print(f'type of now_with_tz: {type(now_with_tz)}')

#now_formatted = now_with_tz.strftime("%d.%m.%Y")
#print(f'now_formatted: {now_formatted}')
#print(f'type of now_formatted: {type(now_formatted)}')

now_parsed = datetime.datetime.strptime("29.01.2022", "%d.%m.%Y")
print(f'now_parsed: {now_parsed}')
#print(f'type of now_parsed: {type(now_parsed)}')


now_plus_week = now_parsed + relativedelta(weeks=+5)
print('now + week', now_plus_week)
#print('type of now_plus_week', type(now_plus_week))

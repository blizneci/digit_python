import pytz
import datetime


timezone = pytz.timezone("Europe/Moscow")
now = timezone.localize(datetime.datetime.now())

with open("/tmp/now.txt", "a") as f:
    f.write(f"Now: {now.hour:02d}:{now.minute:02d}:{now.second:02d}\n")
    if now.minute == 0:
        f.write("Начался новый час\n")
    elif now.minute % 10 == 0:
        f.write("Новые десять минут\n")
    elif now.minute % 15 == 0:
        f.write("Новая четверть часа\n")


import calendar
import datetime


def at_weekend():
    now = datetime.datetime.now()
    weekday = now.weekday()
    hour = now.hour
    minute = now.minute
    if weekday == 4 and (hour > 16 or (hour == 16 and minute >= 0)):
        return True
    elif weekday == 5:
        return True
    elif weekday == 6:
        return True
    elif weekday == 0 and (hour < 9 or (hour == 9 and minute < 30)):
        return True
    return False


def end_of_month():
    today = datetime.date.today()
    _, last_day = calendar.monthrange(today.year, today.month)
    return today.day == last_day

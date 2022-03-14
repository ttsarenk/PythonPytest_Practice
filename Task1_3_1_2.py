from datetime import datetime
from re import search
import datetime
import pytz


# 2) Написать функцию, которая будет принимать на вход названия двух городов из all_timezones
# и возвращать время в этих городах и разницу во времени.
def get_city_time(city):
    tz_list = pytz.all_timezones
    upd_city = " "
    for x in tz_list:
        if search(city, x):
            upd_city = x
        else:
            pass
    tz_city = pytz.timezone(upd_city)
    dt_city = datetime.datetime.now(tz_city)
    dtf_city = datetime.datetime.now(tz_city).strftime("%d-%b-%Y, %H:%M:%S")
    print(city, dtf_city)
    time_city = datetime.timedelta(days=dt_city.day, hours=dt_city.hour, minutes=dt_city.minute,
                                   seconds=dt_city.second)
    return time_city


def get_delta(city1, city2):
    print("\nThe datetime for provided cities:")
    try:
        city1 = get_city_time(city1)
    except:
        print("The 1st city wasn't found.")
    try:
        city2 = get_city_time(city2)
    except:
        print("The 2nd city wasn't found.")
    if city1 >= city2:
        delta = city1 - city2
    else:
        delta = city2 - city1
    print("***\nThe time difference is:", delta)


if __name__ == '__main__':
    try:
        get_delta("New_York", "Kiev")
    except:
        print("Error: one or both cities weren't found. Please, check the spelling and try again.")
    else:
        print("\n\n[Code was successfully executed]")

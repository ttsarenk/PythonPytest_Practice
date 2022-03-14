from datetime import datetime
from datetime import timedelta
import datetime


# 1) Найти 10 ближайших будущих дат пятниц 13-го
def find_fri_13():
    now_date = datetime.date.today()

    if now_date.isoweekday() < 5:
        for i in range(7):
            now_date += timedelta(days=1)
            i += 1
            if now_date.isoweekday() == 5:
                break
    elif now_date.isoweekday() > 5:
        for i in range(7):
            now_date -= timedelta(days=1)
            i += 1
            if now_date.isoweekday() == 5:
                break
    elif now_date.isoweekday() == 5:
        now_date = datetime.date.today()
    else:
        pass

    print("\nThe first 10 dates which are Fridays 13th are:")
    k = 1
    while k <= 10:
        now_date += timedelta(weeks=1)
        if now_date.day == 13:
            print(k, now_date.strftime("%Y, %B, %d, %A"))
            k += 1
        else:
            pass


if __name__ == '__main__':
    find_fri_13()

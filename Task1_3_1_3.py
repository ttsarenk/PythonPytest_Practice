from datetime import datetime
from collections import namedtuple
import datetime
import math


# 3) Написать функцию, которая будет принимать на вход дату рождения человека
# в формате день-месяц-год, например 29-07-1988, и в return возвращать namedtuple c возрастом и знаком зодиака
def get_age_and_zodiac_sign(string):
    delta = 0
    current = datetime.datetime.now()
    dob = datetime.datetime.strptime(string, "%d-%m-%Y")
    if current >= dob:
        delta = current - dob
    else:
        print("Please, enter Date of Birth which is less or equals the current day.")
    age = math.floor(delta.days / 365.2425)

    zodiac_sign = ""
    if (dob.strftime("%B") == "March" and dob.day in range(21, 32)) or (
            dob.strftime("%B") == "April" and dob.day in range(1, 20)):
        zodiac_sign = "Aries"
    elif (dob.strftime("%B") == "April" and dob.day in range(20, 31)) or (
            dob.strftime("%B") == "May" and dob.day in range(1, 21)):
        zodiac_sign = "Taurus"
    elif (dob.strftime("%B") == "May" and dob.day in range(21, 32)) or (
            dob.strftime("%B") == "June" and dob.day in range(1, 22)):
        zodiac_sign = "Gemini"
    elif (dob.strftime("%B") == "June" and dob.day in range(22, 31)) or (
            dob.strftime("%B") == "July" and dob.day in range(1, 23)):
        zodiac_sign = "Cancer"
    elif (dob.strftime("%B") == "July" and dob.day in range(23, 32)) or (
            dob.strftime("%B") == "August" and dob.day in range(1, 23)):
        zodiac_sign = "Leo"
    elif (dob.strftime("%B") == "August" and dob.day in range(23, 32)) or (
            dob.strftime("%B") == "September" and dob.day in range(1, 23)):
        zodiac_sign = "Virgo"
    elif (dob.strftime("%B") == "September" and dob.day in range(23, 31)) or (
            dob.strftime("%B") == "October" and dob.day in range(1, 24)):
        zodiac_sign = "Libra"
    elif (dob.strftime("%B") == "October" and dob.day in range(24, 32)) or (
            dob.strftime("%B") == "November" and dob.day in range(1, 22)):
        zodiac_sign = "Scorpius"
    elif (dob.strftime("%B") == "November" and dob.day in range(22, 31)) or (
            dob.strftime("%B") == "December" and dob.day in range(1, 22)):
        zodiac_sign = "Sagittarius"
    elif (dob.strftime("%B") == "December" and dob.day in range(22, 32)) or (
            dob.strftime("%B") == "January" and dob.day in range(1, 20)):
        zodiac_sign = "Capricornus"
    elif (dob.strftime("%B") == "January" and dob.day in range(20, 32)) or (
            dob.strftime("%B") == "February" and dob.day in range(1, 19)):
        zodiac_sign = "Aquarius"
    elif (dob.strftime("%B") == "February" and dob.day in range(19, 30)) or (
            dob.strftime("%B") == "March" and dob.day in range(1, 21)):
        zodiac_sign = "Pisces"
    else:
        print("Unexpected error occurred.")

    Age_Zodiac = namedtuple("Age_Zodiac", "Age Zodiac")
    age_zodiac = Age_Zodiac(age, zodiac_sign)
    return age_zodiac


if __name__ == '__main__':
    try:
        dob_input = str(input("\nEnter your Date of Birth in format dd-mm-yyyy: "))
        user_data = get_age_and_zodiac_sign(dob_input)
        print(user_data)
    except:
        print("Error. Please, recheck Date of Birth and/or its format.")
    else:
        print("\n\n[Code was successfully executed]")

from datetime import date

import sys

al_multiplier = {
    'S': 1.2,
    'LA': 1.375,
    'A': 1.462,
    'VA': 1.55
}


def calculatecalories(gender, start_weight, height, birth_date, activity_level):
    age = calculate_age(birth_date)
    BOO = 10 * float(start_weight) + 6.25 * float(height) - 5 * float(age) + gendercoeff(gender)
    calories = BOO * al_multiplier[activity_level]

    return calories


def gendercoeff(gender):
    if gender == 'M':
        return 5.0
    else:
        return -161.0


def calculate_age(born):
    today = date.today()
    years_difference = today.year - born.year
    is_before_birthday = (today.month, today.day) < (born.month, born.day)
    elapsed_years = years_difference - int(is_before_birthday)
    return elapsed_years

# the birthday paradox, also called the birthday problem, is the surprisingly high probability that two
# people will have the same birthday even in a small group of people. In a group of 70 people, there's
# a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, there's
# 50 percent chance of a matching birthday.This program performs several probability experiments to determine the
# percentages for groups of different sizes. We call these types of experiments,
# in which we conuct multiple random trials to undersand the likely outcomes, Monte Carlo experiments

import datetime
import random


def generate_birthdays(numofbdays):
    birthdays = []
    startdate = datetime.date(2021, 1, 1)
    for i in range(numofbdays):
        delta = datetime.timedelta(random.randint(1, 364))
        birthday = startdate + delta
        birthdays.append(birthday)
    return birthdays


b = generate_birthdays(1000000)


def get_matching_birthdays(b):
    if len(b) == set(b):
        return "no match"
    for a, birthdayA in enumerate(b):
        for b, birthdayB in enumerate(b[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

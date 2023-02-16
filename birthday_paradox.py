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
        delta = datetime.timedelta(random.randint(1, 365))
        birthday = startdate + delta
        birthdays.append(birthday)
    return birthdays


def get_matching_birthdays(b):
    if len(b) == len(set(b)):
        return None
    for a, birthdayA in enumerate(b):
        for j, birthdayB in enumerate(b[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


#
# month_name = b[1].month
# print(month_name)
# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
 
  The Birthday Paradox shows us that in a group of N people, the odds
  that two of them have matching birthdays is surprisingly large.
  This program does a Monte Carlo simulation (that is, repeated random
  simulations) to explore this concept.
 
  (It's not actually a paradox, it's just a surprising result.)
  ''')
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("how many birthdays do you want to generate")
    response = input("enter the number of birthdays you want to generate(MAX 100):")
    if int(response) <= 100 and response.isdecimal():
        number_of_bdays = int(response)
        break

print("here are the number of birthdays you requested")
birthdays = generate_birthdays(number_of_bdays)
for i, b_day in enumerate(birthdays):
    if i != 0:
        month_name = MONTHS[b_day.month - 1]
        birthday_text = "{}{}".format(month_name, b_day.day)
        print(birthday_text, end=",")
print(end="\n")
match = get_matching_birthdays(birthdays)
if match == None:
    print("no mathch found")
else:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print(f"multiple people have a birthday on this date  {dateText}")
    print(
        "............................................................................................................")
# let's run through 100_000 simulations
print(f"running through 100_000 simulations....by generating {number_of_bdays} random birthdays 100_0000 times")
birthday_match = 0
for i in range(100000):
    test_birthdays = generate_birthdays(number_of_bdays)
    if i % 10000 == 0:
        print(f'{i} simulations run...\n')
    if get_matching_birthdays(test_birthdays) != None:
        birthday_match += 1
# Display simulation results:
probability = round(birthday_match / 100_000 * 100, 2)
print('Out of 100,000 simulations of', number_of_bdays, 'people, there was a')
print('matching birthday in that group', birthday_match, 'times. This means')
print('that', number_of_bdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')

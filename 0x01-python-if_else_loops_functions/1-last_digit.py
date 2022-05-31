#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_cpy = number

if (num_cpy < 0):
    last_digit = (-1 * num_cpy) % 10
else:
    last_digit = number % 10

while 1:
    last_digit = last_digit % 10
    if (last_digit >= 0) and (last_digit <= 9):
        break
    else:
        continue

if (number < 0):
    last_digit = last_digit * -1

print("Last digit of {} is {} ".format(number, last_digit), end='')
if (last_digit > 5):
    print("and is greater than 5")
elif (last_digit == 0):
    print("and is 0")
elif (last_digit < 6) and (last_digit != 0):
    print("and is less than 6 and not 0")

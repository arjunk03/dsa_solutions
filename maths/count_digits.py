"""
Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

    A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
    Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.

Geeks for geeks :  https://www.geeksforgeeks.org/problems/count-digits5716/1
"""


def evenly_divides(n):
    new = n
    cnt = 0
    while new > 0:
        dig = new % 10

        if dig == 0:
            new = new // 10
            continue

        if n % dig == 0:
            cnt += 1

        new = new // 10

    return cnt


a = 12
print(evenly_divides(a))

a = 1025
print(evenly_divides(a))

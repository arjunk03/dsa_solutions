import math


def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    i = 1
    divs = 0
    while i <= math.sqrt(n):
        print(i, n // i)
        if n % i == 0:
            divs += i + n // i
        i += 1

    return divs


a = 4
print(sumOfAllDivisors(a))


a = 8
print(sumOfAllDivisors(a))

def armstrongNumber(n):
    # code here
    nm = n
    res = 0
    while n > 0:
        digit = n % 10
        res += digit * digit * digit

        n //= 10

    return True if res == nm else False


a = 153
print(armstrongNumber(a))

a = 372
print(armstrongNumber(a))

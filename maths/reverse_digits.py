def rev_dig(n):
    rev = 0
    sign = -1 if n < 0 else 1
    n *= sign

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return 0 if rev < -(2**31) or rev > 2**31 - 1 else rev * sign


a = 123
print(rev_dig(a))

a = -123
print(rev_dig(a))

a = 120
print(rev_dig(a))

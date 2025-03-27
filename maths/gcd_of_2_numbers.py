def gcd(m, n):
    hcf = 1

    i = 1
    while i <= min(m, n):
        if m % i == 0 and n % i == 0:
            hcf = i
        i += 1

    return hcf


a = 12
b = 4
print(gcd(a, b))

a = 36
b = 12
print(gcd(a, b))

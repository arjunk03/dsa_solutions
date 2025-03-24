def check(x):
    actual = x
    ans = 0
    if x < 0:
        return False

    while x:
        ans = ans * 10 + x % 10
        x //= 10

    return True if actual == ans else False


a = 121
print(check(a))

a = -121
print(check(a))

a = 10
print(check(a))

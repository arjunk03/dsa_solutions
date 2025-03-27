def factorialNumbers(n):
    # code here

    fact = 1
    i = 1
    ans = []

    while fact <= n:
        ans.append(fact)
        i += 1
        fact = fact * i
    return ans


a = 6
print(factorialNumbers(a))

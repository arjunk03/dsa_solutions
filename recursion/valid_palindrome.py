def isPalindrome(s: str) -> bool:
    s = "".join([char.lower() for char in s if char.isalnum()])

    if not s:
        return True

    start = 0
    end = len(s) - 1

    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


a = "Malayalam"
print(isPalindrome(a))

a = "Tetsting the pal"
print(isPalindrome(a))

def valid_anagram(s, t):
    dct_s = {}

    if len(s) != len(t):
        return False

    i = 0
    while i < len(s):
        dct_s[s[i]] = dct_s.get(s[i], 0) + 1
        dct_s[t[i]] = dct_s.get(t[i], 0) - 1

        i += 1

    res = {vl: 0 for vl in dct_s.values() if vl != 0}
    return False if res else True


s = "cat"
t = "act"
print(valid_anagram(s, t))

s = "caa"
t = "act"
print(valid_anagram(s, t))

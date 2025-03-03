from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        anagrams[tuple(count)].append(s)

    return list(anagrams.values())


s = ["cat", "act", "dog", "god", "dog", "act", "cat"]
print(group_anagrams(s))

from collections import Counter, defaultdict


def count_words(text: str) -> dict:
    """This fnction counts the words in a given text and returns a dictionary

    Args:
        text (str): the text to count the words in

    Returns:
        dict: a dictionary with the words as keys and their counts as values
    """
    return Counter(text.split())


ret = count_words(
    "The quick brown fox jumps over the lazy dog. The dog is lazy.")
print(ret)
print(ret["The"])

a = [("apple", 1), ("banana", 2), ("apple", 3)]

grouped = defaultdict(list)

for fruit, num in a:
    grouped[fruit].append(num)

print(grouped)

a = ["apple", "banana", "apple", "apple", "banana", "apple", "apple", "banana"]
strig = "".join(a)

cnt = Counter(strig)
comon = cnt.most_common(1)
print(comon)


users = [
    {"user": "A", "amount": 10},
    {"user": "B", "amount": 20},
    {"user": "A", "amount": 5},
]
grouped = defaultdict(int)
for user in users:
    grouped[user["user"]] += user["amount"]

print((grouped))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 6, 7]
cnt = Counter(a)
print(cnt)

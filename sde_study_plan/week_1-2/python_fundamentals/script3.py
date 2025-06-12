from collections import Counter


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

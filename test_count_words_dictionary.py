import pytest

def count_words(sentence: str) -> dict:
    # convert and separte by spaces
    words = sentence.lower().split()
    # Create a dictionary to hold word counts
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
print(count_words("AWS is great and AWS is fast"))

# testing the count_words function
def test_count_words():
    sentence = "Brasil hexa campeão"
    expected = {
        "Brasil" == 1,
        "hexa" == 1,
        "campeão" == 1
    }
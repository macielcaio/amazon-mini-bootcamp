# import pytest

"""
given a string, parse it into invert her
i will ot use slicing python

“I’ll reverse the string using Python slicing with a step of -1, which is O(n) time and O(n) space for the new string.”
"""

def reverse_string(text: str) -> str:
    return text[::-1]

# @pytest.fixture
# def reversed_text():
#     return reverse_string("Amazon")
#
# def test_reverse_str(reversed_text):
#     assert reversed_text == "nozamA", f"Expected 'nozamA', but got '{reversed_text}'"

print(reverse_string("amazon"))

def reverse_without_spaces():
    no_spaces = ''.join(reverse_string("aws web services").split())
    return no_spaces
print(reverse_without_spaces())


import pytest

# create a list of numbers
def nums_list():
    numbs = [2, 33, 444, 6, 19549, 10, 11, 13, 14, 20, 565, 1000]
    return numbs
print(nums_list())

# return the sum of the even numbers
def show_pair_numbs(numbers: list) -> int:
    soma = sum(num for num in numbers if num % 2 == 0)
    return soma
print(show_pair_numbs(nums_list()))

"""
below i can test function that will make the sum of the even numbers
"""
# testing the sum of the even numbers
def test_show_pair_numbs():
    assert show_pair_numbs(nums_list()) >= 1000, "Expected sum of even numbers to be 1000"

"""
Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
"""


def find_one_integer(numbers):
    freq = dict()

    for num in numbers:
        if num not in freq:
            freq[num] = 1
        elif num in freq:
            freq[num] += 1

    for key in freq:
        if freq[key] == 1:
            return key

    return None


lst = [6, 1, 3, 3, 3, 6, 6]
print(find_one_integer(lst))


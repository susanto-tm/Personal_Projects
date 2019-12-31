"""
Given a list of numbers, return whether any two sums to k.
For example, given [10, 15, 3, 7] and k of 17,return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def solve(arr, k):
    for num in arr:
        if k - num in arr:
            return True

    return False


lst = [10, 15, 3, 7]
m = 17
print(solve(lst, m))

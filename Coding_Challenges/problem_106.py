"""
Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
"""


def jump(arr, i):
    if i == len(arr) - 1:
        return True
    elif i > len(arr) - 1 or arr[i] == 0:
        return False

    # next jump index
    next_i = arr[i]

    if jump(arr, i+next_i):
        return True

    return False


lst = [3, 0, 0, 1, 2, 0, 0]
print(jump(lst, 0))

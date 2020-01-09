"""
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and
are trying to advance to the end. You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.

For example, given the array `[1, 3, 1, 2, 0, 1]`, we can go from indices `0 -> 1 -> 3 -> 5`, so return `true`.

Given the array `[1, 2, 1, 0, 0]`, we can't reach the end, so return `false`.
"""


def is_possible(arr, curr_index):
    end_index = curr_index + arr[curr_index]

    if end_index >= len(arr) or arr[curr_index] == 0:
        return False
    elif end_index == len(arr) - 1:
        return True

    for i in range(end_index, curr_index, -1):
        if is_possible(arr, i):
            return True

    return False


lst = [1, 3, 1, 2, 0, 1]
print(is_possible(lst, 0))

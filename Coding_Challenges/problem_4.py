"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def solve(arr):
    arr.sort()

    for i in range(len(arr) - 1):
        if arr[i] > 0 and arr[i+1] - arr[i] != 1:
            return arr[i] + 1

    return arr[-1] + 1


lst = [3, 4, -1, 1]
print(solve(lst))

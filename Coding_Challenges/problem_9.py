"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""


def solve(arr):
    highest_sum = 0
    for i in range(len(arr)):
        non_adjacent = 0
        for j in range(len(arr)):
            if j != i:
                if i != 0 and i != len(arr) - 1:
                    if j != i-1 and j != i+1:
                        non_adjacent = arr[i] + arr[j]
                elif i == 0:
                    if j != i+1:
                        non_adjacent = arr[i] + arr[j]
                elif i == len(arr) - 1:
                    if j != i-1:
                        non_adjacent = arr[i] + arr[j]

                if non_adjacent > highest_sum:
                    highest_sum = non_adjacent

    return highest_sum


lst = [5, 1, 1, 5]
print(solve(lst))

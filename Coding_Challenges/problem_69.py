"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largest_product(arr):
    if not arr:
        return arr

    largest = -1
    for i in range(len(arr) - 2):
        product = arr[i] * arr[i+1] * arr[i+2]
        if product > largest:
            largest = product

    return largest


lst = [-10, -10, -10, 2]
print(largest_product(lst))

"""
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by
two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""


def rotate_list(arr, k):
    arr.extend(arr[:k])
    del arr[:k]
    return arr


n = 2
lst = [1, 2, 3, 4, 5, 6]
print(rotate_list(lst, n))

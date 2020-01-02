"""
Linear Search
"""


def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i

    return None


lst = [6, 1, 10, 2, 3, 5]
j = 10
print(linear_search(lst, j))

"""
Merge Sort Separate Functions
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr) // 2

    left = merge_sort(arr[:n])
    right = merge_sort(arr[n:])

    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i == len(left):
        res.extend(right[j:])
    else:
        res.extend(left[i:])

    return res


lst = [6, 1, 10, 2, 3, 5]
print(merge_sort(lst))

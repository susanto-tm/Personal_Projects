"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def merge_sorted(arr1, arr2):
    i = j = 0
    res = list()

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res += arr1[i:]
    res += arr2[j:]

    return res


def sort_squares(arr):
    first_pos_index = 0
    for num in arr:
        if num >= 0:
            break
        first_pos_index += 1

    neg_nums = [x ** 2 for x in reversed(arr[:first_pos_index])]
    pos_nums = [x ** 2 for x in arr[first_pos_index:]]

    return merge_sorted(pos_nums, neg_nums)


lst = [-9, -2, 0, 2, 3]
print(sort_squares(lst))

"""
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and
(4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""


def merge(left_with_inv, right_with_inv):
    res = []
    i = j = 0
    left, left_inv = left_with_inv
    right, right_inv = right_with_inv
    inversions = left_inv + right_inv

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            inversions += len(left[i:])  # since left is sorted if right is placed first everything in left is > right
            j += 1

    if i == len(left):
        res.extend(right[j:])
    else:
        res.extend(left[i:])

    return res, inversions


def merge_sort(arr):
    if not arr or len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    res, inversions = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return res, inversions


def count_inversions(arr):
    _, inversions = merge_sort(arr)

    return inversions


lst = [5, 4, 3, 2, 1]
print(count_inversions(lst))

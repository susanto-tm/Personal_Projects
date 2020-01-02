"""
Binary Search
"""


def binary_search(arr, l, r, k):
    if r >= 1:
        mid = (l + r) // 2

        if k == arr[mid]:
            return mid
        elif arr[mid] > k:
            return binary_search(arr, 0, mid-1, k)
        elif k > arr[mid]:
            return binary_search(arr, mid+1, r, k)
    else:
        return -1


lst = [1, 2, 3, 5, 6, 10]
print(binary_search(lst, 0, len(lst) - 1, 10))

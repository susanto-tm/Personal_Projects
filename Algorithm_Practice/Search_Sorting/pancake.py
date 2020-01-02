"""
Pancake Sort
"""


def find_max(arr, n):
    max_idx = 0
    for i in range(n):
        if arr[i] > arr[max_idx]:
            max_idx = i

    return max_idx


def flip_sort(arr):
    n = len(arr)

    while n > 1:
        mi = find_max(arr, n)

        if mi != n - 1:
            arr[:mi+1] = arr[:mi+1][::-1]  # flip up until the index of largest element
            arr[:n] = arr[:n][::-1] # flip array to move largest to the back

        n -= 1


lst = [6, 1, 10, 2, 3, 5]
flip_sort(lst)
print(lst)

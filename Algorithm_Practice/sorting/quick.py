"""
Quick Sort
"""


def partition(arr, l, r):
    pivot = arr[-1]
    i = l  # track element < pivot

    for j in range(l, r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def quick_sort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)

        quick_sort(arr, l, pi-1)
        quick_sort(arr, pi+1, r)


lst = [6, 1, 10, 2, 3, 5]
quick_sort(lst, 0, len(lst) - 1)
print(lst)



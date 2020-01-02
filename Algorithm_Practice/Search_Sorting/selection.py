"""
Selection Sort
"""


def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_idx = i
        for j in range(i+1, len(arr)):
            if arr[smallest_idx] > arr[j]:
                smallest_idx = j
        arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]

    return arr


lst = [6, 1, 10, 2, 3, 5]
print(selection_sort(lst))

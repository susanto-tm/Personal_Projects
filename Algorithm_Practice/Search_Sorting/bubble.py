"""
Bubble Sort
"""


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


lst = [6, 1, 10, 2, 3, 5]
print(bubble_sort(lst))

"""
Insertion Sort
"""


def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1

    return arr


lst = [6, 1, 10, 2, 3, 5]
print(insertion_sort(lst))

"""
Bogo Sort or Permutation Sort
"""
from random import randint


def bogo_sort(arr):
    while is_sorted(arr) is False:
        shuffle(arr)

    return arr


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True


def shuffle(arr):
    for i in range(len(arr)):
        r = randint(0, len(arr) - 1)
        arr[i], arr[r] = arr[r], arr[i]


lst = [6, 1, 10, 2, 3, 5]
print(bogo_sort(lst))

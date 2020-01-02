"""
Heap Sort
"""


def heapify(arr, n, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # build maxheap
    for i in reversed(range(n // 2)):
        heapify(arr, n, i)

    # go through each element and swap largest element
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


lst = [6, 1, 10, 2, 3, 5]
heap_sort(lst)
print(lst)


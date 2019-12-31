"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""


def running_median(arr):
    for i in range(1, len(arr)+1):
        median = get_median(arr[:i])
        print(median if median > median // 1 else int(median))


def get_median(arr):
    arr.sort()
    if len(arr) == 1:
        return arr[0]
    elif len(arr) % 2 == 0:
        mid = (len(arr) // 2) - 1
        return (arr[mid] + arr[mid+1]) / 2
    else:
        mid = len(arr) // 2
        return arr[mid]


lst = [2, 1, 5, 7, 2, 0, 5]
running_median(lst)

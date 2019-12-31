"""
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
"""


def max_of_sub_array(arr, k):
    i = 0
    while i + k != len(arr)+1:
        values = []
        for j in range(i, i+k):
            values.append(arr[j])

        print(max(values))
        i += 1


lst = [10, 5, 2, 7, 8, 7]
max_of_sub_array(lst, 2)

"""
Write a program that checks whether an integer is a palindrome. For example, `121` is a palindrome,
as well as `888`. `678` is not a palindrome. Do not convert the integer into a string.
"""


def is_palindrome(num):
    reverse_num = num
    rev = 0

    while reverse_num > 0:
        rev = rev * 10 + reverse_num % 10
        reverse_num //= 10

    return num == rev


n = 121
print(is_palindrome(n))

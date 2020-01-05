"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def sum_digit(digits):
    total = 0
    while digits > 0:
        total = total + digits % 10
        digits //= 10

    return total


def find_perfect_number(digits):
    total = sum_digit(digits)

    n = 10 - total

    return str(digits) + str(n)




print(find_perfect_number(1))

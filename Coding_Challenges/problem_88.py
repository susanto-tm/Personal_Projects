"""
Implement division of two positive integers without using the division, multiplication,
or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""


def divide(dividend, divisor):
    if not divisor:
        return

    curr_sum = 0
    quotient = 0

    while curr_sum <= dividend:  # go one extra to be the same for all numbers
        quotient += 1
        curr_sum += divisor

    return quotient - 1


assert not divide(1, 0)
assert divide(18, 2) == 9
assert divide(1, 2) == 0
assert divide(3, 2) == 1
assert divide(99, 2) == 49



"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
* If `n` is even, the next number in the sequence is `n / 2`
* If `n` is odd, the next number in the sequence is `3n + 1`
It is conjectured that every such sequence eventually reaches the number `1`. Test this conjecture.

Bonus: What input `n <= 1000000` gives the longest sequence?
"""


def collatz_sequence(num):
    while num != 1:
        if num % 2 == 0:
            num //= 2
        elif num % 2 != 0:
            num = 3 * num + 1

    return True


n = 9
print(collatz_sequence(n))

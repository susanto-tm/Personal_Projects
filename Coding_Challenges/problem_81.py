"""
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], } then "23" should
return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
"""

output = []
phones = {'2': ['a', 'b', 'c'],
          '3': ['d', 'e', 'f'],
          '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'],
          '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'],
          '9': ['w', 'x', 'y', 'z']}


def digits_to_letters(combination, next_digit):
    if len(next_digit) == 0:
        output.append(combination)
    else:
        for letter in phones[next_digit[0]]:
            digits_to_letters(combination + letter, next_digit[1:])


digits_to_letters("", "23")
print(output)

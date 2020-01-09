"""
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string.
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""


def count_pattern_occurrence(string, pattern):
    n = len(pattern)

    return [i for i in range(len(string)) if string[i:i+n] == pattern]


full_string = "abracadabra"
patt = "abr"
print(count_pattern_occurrence(full_string, patt))

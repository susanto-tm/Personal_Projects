"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def longest_substring(sub, k):
    if not sub:
        return ""
    elif len(sub) <= k:
        return sub
    elif k == 1:
        return sub[0]

    distinct_char = 0
    seen_chars = set()
    remaining_string = None

    first_char = sub[0]
    second_char_count = 0
    # check where second character occurs
    while sub[second_char_count] == first_char:
        second_char_count += 1

    candidate = sub
    for idx, char in enumerate(sub):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char += 1

        if distinct_char > k:
            candidate = sub[:idx]
            remaining_string = sub[second_char_count:]
            break

    longest_remaining = longest_substring(remaining_string, k)

    if len(candidate) < len(longest_remaining):
        longest_sub = longest_remaining
    else:
        longest_sub = candidate
    return longest_sub


s = "abcba"
distinct = 2
print(longest_substring(s, distinct))

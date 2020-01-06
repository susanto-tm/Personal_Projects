"""
Given a string of words delimited by spaces, reverse the words in string. For example,
given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def reverse_words(word):
    return ' '.join(word.split()[::-1])


print(reverse_words("hello world here HI"))


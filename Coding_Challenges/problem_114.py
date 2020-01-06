"""
Given a string and a set of delimiters, reverse the words in the string while maintaining
the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""


def reverse_words(string, delimiters):
    words = list()
    delim = list()
    delim_position = list()

    start = 0
    i = 0

    while i < len(string):
        char = string[i]

        if char in delimiters:
            word = string[start:i]
            if i - start > 1:
                words.append(word)
            delim.append(char)
            delim_position.append(len(words) + len(delim) - 1)
            start = i + 1

        i += 1

    # get last word if exists
    if i - start > 1:
        words.append(string[start:i])

    words.reverse()  # reverse word order

    reversed_order = list()
    word_index = 0
    delim_index = 0

    for i in range(len(words) + len(delim)):
        if delim_index < len(delim_position) and delim_position[delim_index] == i:
            reversed_order.append(delim[delim_index])
            delim_index += 1
        else:
            reversed_order.append(words[word_index])
            word_index += 1

    return "".join(reversed_order)


print(reverse_words("hello//world:here/", {"/", ":"}))


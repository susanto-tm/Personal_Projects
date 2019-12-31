"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def str_reconstruction(complete, sets):
    if not sets or not complete:
        return []

    word_set = set(sets)
    sentence_words = list()
    for i in range(len(complete)):
        if complete[0:i+1] in word_set:
            sentence_words.append(complete[0:i+1])
            word_set.remove(complete[0:i+1])
            sentence_words += str_reconstruction(complete[i+1:], word_set)

    return sentence_words


set_of_word = ['the', 'quick', 'brown', 'fox']
word_str = "thequickbrownfox"
print(str_reconstruction(word_str, set_of_word))

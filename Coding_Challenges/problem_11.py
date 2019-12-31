"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def generate_dict(query, words):
    query_len = len(query)
    possible_combinations = {}

    for word in words:
        prefix = word[:query_len]
        if prefix not in possible_combinations:
            possible_combinations[prefix] = [word]
        elif prefix in possible_combinations:
            possible_combinations[prefix].append(word)

    return possible_combinations


def solve(query, words):
    combinations = generate_dict(query, words)
    if query not in combinations:
        return []
    else:
        return [x for x in combinations[query]]


query_str = 'de'
word_dict = ['dog', 'deer', 'deal']

assert solve('de', ['dog', 'deer', 'deal']) == ['deer', 'deal']
assert solve("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert solve("ae", ["cat", "car", "cer"]) == []
assert solve("ae", []) == []



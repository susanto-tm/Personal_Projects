"""
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""


def is_palindrome(string):
    return bool(string) and string == string[::-1]


def make_palindrome(string, num_delete):
    if is_palindrome(string):
        return True
    if not num_delete:
        return False

    for i, _ in enumerate(string):
        new_string = string[:i] + string[i+1]
        if make_palindrome(new_string, num_delete - 1):
            return True

    return False


print(make_palindrome("waterrfetawx", 2))


def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""

    return word == word[::-1]

is_palindrome("foo")
is_palindrome("civic")
is_palindrome("biko")

# Recursive is_palindrome():

def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""

    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

 # Base cases:
is_palindrome("")
is_palindrome("a")

# Recursive cases:

is_palindrome("foo")
is_palindrome("biko")
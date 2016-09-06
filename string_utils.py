"""
String utility functions
"""


def reverse_string(s):
    """Reverse a string"""
    return s[::-1]


def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and spaces)"""
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """Count the number of vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def capitalize_words(s):
    """Capitalize the first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())


def remove_duplicates(s):
    """Remove duplicate characters from a string while preserving order"""
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


def count_words(s):
    """Count the number of words in a string"""
    return len(s.split())


def truncate(s, max_length, suffix='...'):
    """Truncate a string to max_length, adding suffix if truncated"""
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix

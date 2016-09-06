"""
Unit tests for string_utils module
"""
import unittest
from string_utils import (
    reverse_string, is_palindrome, count_vowels,
    capitalize_words, remove_duplicates, count_words, truncate
)


class TestReverseString(unittest.TestCase):
    """Test reverse_string function"""

    def test_reverse_simple_string(self):
        """Test reversing simple strings"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_reverse_empty_string(self):
        """Test reversing empty string"""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        """Test reversing single character"""
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Z"), "Z")

    def test_reverse_with_spaces(self):
        """Test reversing strings with spaces"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("a b c"), "c b a")

    def test_reverse_palindrome(self):
        """Test reversing palindromes"""
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("madam"), "madam")


class TestIsPalindrome(unittest.TestCase):
    """Test is_palindrome function"""

    def test_simple_palindromes(self):
        """Test with simple palindromes"""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("level"))

    def test_non_palindromes(self):
        """Test with non-palindromes"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces"""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("nurses run"))
        self.assertTrue(is_palindrome("taco cat"))

    def test_palindrome_case_insensitive(self):
        """Test that palindrome check is case insensitive"""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("A"))

    def test_empty_and_single_char(self):
        """Test with empty string and single character"""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))

    def test_complex_palindromes(self):
        """Test complex palindromes with multiple spaces"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))


class TestCountVowels(unittest.TestCase):
    """Test count_vowels function"""

    def test_count_vowels_simple(self):
        """Test counting vowels in simple strings"""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("python"), 1)

    def test_count_vowels_all_vowels(self):
        """Test with strings containing all vowels"""
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_count_vowels_no_vowels(self):
        """Test with strings containing no vowels"""
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_mixed_case(self):
        """Test counting vowels with mixed case"""
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("Programming"), 3)

    def test_count_vowels_with_spaces(self):
        """Test counting vowels in strings with spaces"""
        self.assertEqual(count_vowels("the quick brown fox"), 5)
        self.assertEqual(count_vowels("education is important"), 9)


class TestCapitalizeWords(unittest.TestCase):
    """Test capitalize_words function"""

    def test_capitalize_simple(self):
        """Test capitalizing simple strings"""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")

    def test_capitalize_already_capitalized(self):
        """Test with already capitalized strings"""
        self.assertEqual(capitalize_words("Hello World"), "Hello World")
        self.assertEqual(capitalize_words("HELLO WORLD"), "Hello World")

    def test_capitalize_single_word(self):
        """Test capitalizing single word"""
        self.assertEqual(capitalize_words("hello"), "Hello")
        self.assertEqual(capitalize_words("python"), "Python")

    def test_capitalize_empty_string(self):
        """Test with empty string"""
        self.assertEqual(capitalize_words(""), "")

    def test_capitalize_mixed_case(self):
        """Test with mixed case input"""
        self.assertEqual(capitalize_words("hElLo WoRlD"), "Hello World")
        self.assertEqual(capitalize_words("pYtHoN"), "Python")


class TestRemoveDuplicates(unittest.TestCase):
    """Test remove_duplicates function"""

    def test_remove_duplicates_simple(self):
        """Test removing duplicates from simple strings"""
        self.assertEqual(remove_duplicates("hello"), "helo")
        self.assertEqual(remove_duplicates("programming"), "progamin")

    def test_remove_duplicates_no_duplicates(self):
        """Test with strings that have no duplicates"""
        self.assertEqual(remove_duplicates("abc"), "abc")
        self.assertEqual(remove_duplicates("python"), "python")

    def test_remove_duplicates_all_same(self):
        """Test with strings where all characters are the same"""
        self.assertEqual(remove_duplicates("aaaa"), "a")
        self.assertEqual(remove_duplicates("bbbbbb"), "b")

    def test_remove_duplicates_empty(self):
        """Test with empty string"""
        self.assertEqual(remove_duplicates(""), "")

    def test_remove_duplicates_preserves_order(self):
        """Test that order is preserved"""
        self.assertEqual(remove_duplicates("abcabc"), "abc")
        self.assertEqual(remove_duplicates("aabbcc"), "abc")


class TestCountWords(unittest.TestCase):
    """Test count_words function"""

    def test_count_words_simple(self):
        """Test counting words in simple strings"""
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("python programming language"), 3)

    def test_count_words_single_word(self):
        """Test with single word"""
        self.assertEqual(count_words("hello"), 1)
        self.assertEqual(count_words("python"), 1)

    def test_count_words_empty_string(self):
        """Test with empty string"""
        self.assertEqual(count_words(""), 0)

    def test_count_words_multiple_spaces(self):
        """Test with multiple spaces between words"""
        self.assertEqual(count_words("hello  world"), 2)
        self.assertEqual(count_words("one   two    three"), 3)

    def test_count_words_sentence(self):
        """Test with longer sentences"""
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog"), 9)


class TestTruncate(unittest.TestCase):
    """Test truncate function"""

    def test_truncate_long_string(self):
        """Test truncating strings longer than max_length"""
        self.assertEqual(truncate("hello world", 8), "hello...")
        self.assertEqual(truncate("python programming", 10), "python ...")

    def test_truncate_short_string(self):
        """Test with strings shorter than max_length"""
        self.assertEqual(truncate("hello", 10), "hello")
        self.assertEqual(truncate("hi", 5), "hi")

    def test_truncate_exact_length(self):
        """Test with string exactly at max_length"""
        self.assertEqual(truncate("hello", 5), "hello")
        self.assertEqual(truncate("world", 5), "world")

    def test_truncate_custom_suffix(self):
        """Test truncating with custom suffix"""
        self.assertEqual(truncate("hello world", 8, ">>"), "hello >>")
        self.assertEqual(truncate("python programming", 10, "[...]"), "pytho[...]")

    def test_truncate_empty_string(self):
        """Test with empty string"""
        self.assertEqual(truncate("", 5), "")

    def test_truncate_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(truncate("hello world", 3), "...")
        self.assertEqual(truncate("test", 4, "..."), "test")


if __name__ == '__main__':
    unittest.main()

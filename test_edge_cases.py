"""
Additional edge case and boundary value tests for comprehensive coverage
"""
import unittest
from calculator import (
    add, subtract, multiply, divide, power,
    is_even, is_prime, factorial, fibonacci
)
from string_utils import (
    reverse_string, is_palindrome, count_vowels,
    capitalize_words, remove_duplicates, count_words, truncate
)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Edge cases and boundary value tests for calculator"""

    def test_add_very_large_numbers(self):
        """Test addition with very large numbers"""
        large = 10**100
        self.assertEqual(add(large, large), 2 * large)
        self.assertEqual(add(large, 1), large + 1)

    def test_add_very_small_floats(self):
        """Test addition with very small floating point numbers"""
        small = 1e-10
        self.assertAlmostEqual(add(small, small), 2 * small, places=15)

    def test_multiply_by_zero(self):
        """Test multiplication by zero with various numbers"""
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(1000000, 0), 0)
        self.assertEqual(multiply(-999, 0), 0)

    def test_multiply_large_numbers(self):
        """Test multiplication of large numbers"""
        self.assertEqual(multiply(10**10, 10**10), 10**20)

    def test_divide_very_small_result(self):
        """Test division resulting in very small numbers"""
        self.assertAlmostEqual(divide(1, 10**10), 1e-10)

    def test_divide_same_numbers(self):
        """Test dividing a number by itself"""
        self.assertEqual(divide(5, 5), 1)
        self.assertEqual(divide(-7, -7), 1)
        self.assertEqual(divide(100, 100), 1)

    def test_power_large_exponents(self):
        """Test power with large exponents"""
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(2, 20), 1048576)
        self.assertEqual(power(10, 5), 100000)

    def test_power_fractional_results(self):
        """Test power with fractional exponents"""
        self.assertAlmostEqual(power(4, 0.5), 2.0)
        self.assertAlmostEqual(power(27, 1/3), 3.0, places=5)

    def test_is_even_large_numbers(self):
        """Test is_even with very large numbers"""
        self.assertTrue(is_even(10**100))
        self.assertFalse(is_even(10**100 + 1))

    def test_is_prime_edge_cases(self):
        """Test is_prime with specific edge cases"""
        # Test with perfect squares
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(25))

        # Test numbers just before and after primes
        self.assertTrue(is_prime(23))
        self.assertFalse(is_prime(24))
        self.assertFalse(is_prime(22))

    def test_is_prime_large_primes(self):
        """Test is_prime with larger prime numbers"""
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(103))
        self.assertTrue(is_prime(107))
        self.assertTrue(is_prime(109))
        self.assertTrue(is_prime(113))

    def test_factorial_medium_numbers(self):
        """Test factorial with medium-sized numbers"""
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)

    def test_fibonacci_sequence_properties(self):
        """Test mathematical properties of Fibonacci sequence"""
        # Fibonacci(n) + Fibonacci(n+1) = Fibonacci(n+2)
        for n in range(10):
            self.assertEqual(
                fibonacci(n) + fibonacci(n + 1),
                fibonacci(n + 2)
            )

    def test_fibonacci_large_indices(self):
        """Test Fibonacci with larger indices"""
        self.assertEqual(fibonacci(25), 75025)
        self.assertEqual(fibonacci(30), 832040)

    def test_subtract_zero(self):
        """Test subtraction involving zero"""
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_same_number(self):
        """Test subtracting a number from itself"""
        self.assertEqual(subtract(7, 7), 0)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertEqual(subtract(1000, 1000), 0)

    def test_divide_negative_by_negative(self):
        """Test division of two negative numbers"""
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(-15, -3), 5)

    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(-7, 0), 1)

    def test_power_one_base(self):
        """Test power with base of 1"""
        self.assertEqual(power(1, 5), 1)
        self.assertEqual(power(1, 100), 1)
        self.assertEqual(power(1, 0), 1)


class TestStringUtilsEdgeCases(unittest.TestCase):
    """Edge cases and boundary value tests for string_utils"""

    def test_reverse_unicode_string(self):
        """Test reversing strings with unicode characters"""
        self.assertEqual(reverse_string("café"), "éfac")
        self.assertEqual(reverse_string("👋🌍"), "🌍👋")

    def test_reverse_long_string(self):
        """Test reversing very long strings"""
        long_str = "a" * 10000
        reversed_str = reverse_string(long_str)
        self.assertEqual(len(reversed_str), 10000)
        self.assertEqual(reversed_str, long_str)

    def test_is_palindrome_numbers(self):
        """Test palindrome check with numeric strings"""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("99999"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_single_space(self):
        """Test palindrome with single spaces"""
        self.assertTrue(is_palindrome("a b a"))
        self.assertTrue(is_palindrome("a b c b a"))

    def test_is_palindrome_long_palindrome(self):
        """Test with longer palindromes"""
        long_pal = "a" * 1000 + "b" + "a" * 1000
        self.assertTrue(is_palindrome(long_pal))

    def test_count_vowels_only_consonants(self):
        """Test counting vowels in strings with only consonants"""
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)
        self.assertEqual(count_vowels("BCDFG"), 0)

    def test_count_vowels_repeated(self):
        """Test counting repeated vowels"""
        self.assertEqual(count_vowels("aaaaaa"), 6)
        self.assertEqual(count_vowels("eeeeeeeeee"), 10)

    def test_count_vowels_special_characters(self):
        """Test vowel counting with special characters"""
        self.assertEqual(count_vowels("hello@world.com"), 4)
        self.assertEqual(count_vowels("test#123$abc"), 2)

    def test_capitalize_words_numbers(self):
        """Test capitalizing words with numbers"""
        self.assertEqual(capitalize_words("test 123 word"), "Test 123 Word")
        self.assertEqual(capitalize_words("abc 456 def"), "Abc 456 Def")

    def test_capitalize_words_special_chars(self):
        """Test capitalizing with special characters"""
        self.assertEqual(capitalize_words("hello-world"), "Hello-world")

    def test_remove_duplicates_long_string(self):
        """Test removing duplicates from long strings"""
        input_str = "abcabc" * 100
        result = remove_duplicates(input_str)
        self.assertEqual(result, "abc")
        self.assertEqual(len(result), 3)

    def test_remove_duplicates_special_chars(self):
        """Test removing duplicates with special characters"""
        self.assertEqual(remove_duplicates("hello!!!"), "helo!")
        self.assertEqual(remove_duplicates("test###test"), "tes#")

    def test_count_words_tabs_and_newlines(self):
        """Test word counting with tabs and newlines"""
        self.assertEqual(count_words("hello\tworld"), 2)
        self.assertEqual(count_words("one\ntwo\nthree"), 3)

    def test_count_words_leading_trailing_spaces(self):
        """Test word counting with leading/trailing spaces"""
        self.assertEqual(count_words("  hello  "), 1)
        self.assertEqual(count_words("   hello world   "), 2)

    def test_truncate_unicode(self):
        """Test truncating strings with unicode"""
        result = truncate("café restaurant", 8)
        self.assertLessEqual(len(result), 8)

    def test_truncate_exactly_at_suffix_boundary(self):
        """Test truncation exactly at suffix length"""
        self.assertEqual(truncate("hello world", 5), "he...")
        self.assertEqual(truncate("test", 3), "...")

    def test_truncate_empty_suffix(self):
        """Test truncation with empty suffix"""
        self.assertEqual(truncate("hello world", 5, ""), "hello")

    def test_truncate_longer_suffix(self):
        """Test with suffix longer than max_length"""
        result = truncate("hello", 3, "[truncated]")
        # Should handle gracefully
        self.assertIsInstance(result, str)

    def test_capitalize_words_single_letter_words(self):
        """Test capitalizing single letter words"""
        self.assertEqual(capitalize_words("a b c"), "A B C")
        self.assertEqual(capitalize_words("i am a student"), "I Am A Student")

    def test_reverse_string_with_numbers(self):
        """Test reversing strings with numbers"""
        self.assertEqual(reverse_string("abc123"), "321cba")
        self.assertEqual(reverse_string("2023test"), "tset3202")


class TestBoundaryValues(unittest.TestCase):
    """Tests focusing on boundary values"""

    def test_factorial_boundary(self):
        """Test factorial at important boundaries"""
        # 0! and 1! are both 1
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_fibonacci_boundary(self):
        """Test Fibonacci at boundaries"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_is_prime_boundary(self):
        """Test prime checking at boundaries"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))  # Smallest prime
        self.assertTrue(is_prime(3))

    def test_division_by_one(self):
        """Test division by one"""
        self.assertEqual(divide(10, 1), 10)
        self.assertEqual(divide(-5, 1), -5)
        self.assertEqual(divide(0, 1), 0)

    def test_power_identity(self):
        """Test power with exponent 1"""
        self.assertEqual(power(5, 1), 5)
        self.assertEqual(power(100, 1), 100)
        self.assertEqual(power(-7, 1), -7)

    def test_empty_string_operations(self):
        """Test all string operations with empty strings"""
        self.assertEqual(reverse_string(""), "")
        self.assertTrue(is_palindrome(""))
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(capitalize_words(""), "")
        self.assertEqual(remove_duplicates(""), "")
        self.assertEqual(count_words(""), 0)
        self.assertEqual(truncate("", 5), "")

    def test_single_character_operations(self):
        """Test string operations with single characters"""
        self.assertEqual(reverse_string("a"), "a")
        self.assertTrue(is_palindrome("a"))
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(capitalize_words("a"), "A")
        self.assertEqual(remove_duplicates("a"), "a")
        self.assertEqual(count_words("a"), 1)
        self.assertEqual(truncate("a", 5), "a")


class TestTypeConsistency(unittest.TestCase):
    """Test type consistency and return types"""

    def test_arithmetic_return_types(self):
        """Test that arithmetic operations return correct types"""
        self.assertIsInstance(add(1, 2), int)
        self.assertIsInstance(add(1.0, 2.0), float)
        self.assertIsInstance(multiply(3, 4), int)
        self.assertIsInstance(divide(10, 2), (int, float))

    def test_boolean_return_types(self):
        """Test that boolean functions return booleans"""
        self.assertIsInstance(is_even(4), bool)
        self.assertIsInstance(is_prime(5), bool)
        self.assertIsInstance(is_palindrome("test"), bool)

    def test_string_return_types(self):
        """Test that string functions return strings"""
        self.assertIsInstance(reverse_string("test"), str)
        self.assertIsInstance(capitalize_words("test"), str)
        self.assertIsInstance(remove_duplicates("test"), str)
        self.assertIsInstance(truncate("test", 5), str)

    def test_integer_return_types(self):
        """Test that integer functions return integers"""
        self.assertIsInstance(factorial(5), int)
        self.assertIsInstance(fibonacci(10), int)
        self.assertIsInstance(count_vowels("test"), int)
        self.assertIsInstance(count_words("test"), int)


if __name__ == '__main__':
    unittest.main()

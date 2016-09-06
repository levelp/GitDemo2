"""
Error handling and exception tests
"""
import unittest
from calculator import divide, factorial, fibonacci


class TestErrorHandling(unittest.TestCase):
    """Test error handling and exceptions"""

    def test_divide_by_zero_message(self):
        """Test that divide by zero has correct error message"""
        with self.assertRaises(ValueError) as cm:
            divide(5, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero")

    def test_divide_by_zero_with_zero_numerator(self):
        """Test divide by zero even with zero numerator"""
        with self.assertRaises(ValueError) as cm:
            divide(0, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero")

    def test_divide_by_zero_with_negative(self):
        """Test divide by zero with negative numerator"""
        with self.assertRaises(ValueError) as cm:
            divide(-10, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero")

    def test_factorial_negative_message(self):
        """Test that factorial of negative has correct error message"""
        with self.assertRaises(ValueError) as cm:
            factorial(-1)
        self.assertEqual(
            str(cm.exception),
            "Factorial is not defined for negative numbers"
        )

    def test_factorial_various_negatives(self):
        """Test factorial with various negative numbers"""
        negative_numbers = [-1, -5, -10, -100, -1000]
        for num in negative_numbers:
            with self.assertRaises(ValueError):
                factorial(num)

    def test_fibonacci_negative_message(self):
        """Test that Fibonacci with negative index has correct error message"""
        with self.assertRaises(ValueError) as cm:
            fibonacci(-1)
        self.assertEqual(
            str(cm.exception),
            "Fibonacci is not defined for negative indices"
        )

    def test_fibonacci_various_negatives(self):
        """Test Fibonacci with various negative indices"""
        negative_indices = [-1, -5, -10, -100]
        for idx in negative_indices:
            with self.assertRaises(ValueError):
                fibonacci(idx)

    def test_multiple_exceptions_in_sequence(self):
        """Test that multiple exceptions can be raised properly"""
        # First exception
        with self.assertRaises(ValueError):
            divide(10, 0)

        # Second exception
        with self.assertRaises(ValueError):
            factorial(-5)

        # Third exception
        with self.assertRaises(ValueError):
            fibonacci(-3)

        # All should work independently


class TestInputValidation(unittest.TestCase):
    """Test various input validations"""

    def test_divide_float_denominator_zero(self):
        """Test division by floating point zero"""
        with self.assertRaises(ValueError):
            divide(10.5, 0.0)

    def test_factorial_zero_boundary(self):
        """Test factorial at zero boundary (valid)"""
        # This should NOT raise an error
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_fibonacci_zero_boundary(self):
        """Test Fibonacci at zero boundary (valid)"""
        # This should NOT raise an error
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_error_recovery(self):
        """Test that after an error, functions still work"""
        # Cause an error
        try:
            divide(5, 0)
        except ValueError:
            pass

        # Function should still work afterward
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_factorial_after_error(self):
        """Test factorial works after error"""
        try:
            factorial(-5)
        except ValueError:
            pass

        # Should work fine after error
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_fibonacci_after_error(self):
        """Test Fibonacci works after error"""
        try:
            fibonacci(-10)
        except ValueError:
            pass

        # Should work fine after error
        result = fibonacci(10)
        self.assertEqual(result, 55)


class TestDataTableTests(unittest.TestCase):
    """Data-driven tests using tables of inputs and expected outputs"""

    def test_addition_table(self):
        """Test addition with table of test cases"""
        test_cases = [
            # (a, b, expected)
            (0, 0, 0),
            (1, 1, 2),
            (5, 3, 8),
            (-1, 1, 0),
            (-5, -3, -8),
            (100, 200, 300),
            (1.5, 2.5, 4.0),
        ]

        from calculator import add
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = add(a, b)
                if isinstance(expected, float):
                    self.assertAlmostEqual(result, expected)
                else:
                    self.assertEqual(result, expected)

    def test_multiplication_table(self):
        """Test multiplication with table of test cases"""
        test_cases = [
            # (a, b, expected)
            (0, 5, 0),
            (1, 7, 7),
            (2, 3, 6),
            (-2, 3, -6),
            (-2, -3, 6),
            (10, 10, 100),
            (0.5, 4, 2.0),
        ]

        from calculator import multiply
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = multiply(a, b)
                if isinstance(expected, float):
                    self.assertAlmostEqual(result, expected)
                else:
                    self.assertEqual(result, expected)

    def test_prime_table(self):
        """Test is_prime with table of known values"""
        test_cases = [
            # (n, is_prime)
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (11, True),
            (15, False),
            (17, True),
            (20, False),
            (23, True),
            (29, True),
            (30, False),
        ]

        from calculator import is_prime
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(is_prime(n), expected)

    def test_palindrome_table(self):
        """Test is_palindrome with table of test cases"""
        test_cases = [
            # (string, is_palindrome)
            ("", True),
            ("a", True),
            ("aa", True),
            ("ab", False),
            ("aba", True),
            ("abc", False),
            ("racecar", True),
            ("hello", False),
            ("madam", True),
            ("12321", True),
            ("12345", False),
        ]

        from string_utils import is_palindrome
        for string, expected in test_cases:
            with self.subTest(string=string):
                self.assertEqual(is_palindrome(string), expected)

    def test_vowel_count_table(self):
        """Test count_vowels with table of test cases"""
        test_cases = [
            # (string, vowel_count)
            ("", 0),
            ("a", 1),
            ("e", 1),
            ("i", 1),
            ("o", 1),
            ("u", 1),
            ("bcdfg", 0),
            ("aeiou", 5),
            ("AEIOU", 5),
            ("hello", 2),
            ("world", 1),
            ("python", 1),
            ("programming", 3),
        ]

        from string_utils import count_vowels
        for string, expected in test_cases:
            with self.subTest(string=string):
                self.assertEqual(count_vowels(string), expected)

    def test_factorial_table(self):
        """Test factorial with table of known values"""
        test_cases = [
            # (n, factorial)
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
        ]

        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(factorial(n), expected)

    def test_fibonacci_table(self):
        """Test Fibonacci with table of known values"""
        test_cases = [
            # (n, fibonacci)
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
        ]

        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)

    def test_even_numbers_table(self):
        """Test is_even with table of test cases"""
        test_cases = [
            # (n, is_even)
            (0, True),
            (1, False),
            (2, True),
            (3, False),
            (-2, True),
            (-3, False),
            (100, True),
            (101, False),
        ]

        from calculator import is_even
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(is_even(n), expected)


if __name__ == '__main__':
    unittest.main()

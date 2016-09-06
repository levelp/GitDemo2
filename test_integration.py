"""
Integration tests that test multiple modules working together
"""
import unittest
from calculator import factorial, fibonacci, is_prime
from string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words


class TestIntegration(unittest.TestCase):
    """Integration tests combining calculator and string_utils"""

    def test_factorial_and_string_operations(self):
        """Test factorial results with string operations"""
        result = factorial(5)
        result_str = str(result)
        self.assertEqual(result_str, "120")
        self.assertEqual(reverse_string(result_str), "021")
        self.assertFalse(is_palindrome(result_str))

    def test_fibonacci_sequence_as_string(self):
        """Test creating Fibonacci sequence and analyzing as string"""
        fib_numbers = [fibonacci(i) for i in range(10)]
        fib_str = ' '.join(str(n) for n in fib_numbers)

        # Count words in the string representation
        from string_utils import count_words
        self.assertEqual(count_words(fib_str), 10)

        # Capitalize the string (though numbers don't change)
        capitalized = capitalize_words(fib_str)
        self.assertEqual(capitalized, fib_str)

    def test_prime_numbers_string_analysis(self):
        """Test finding primes and analyzing their string properties"""
        primes = [n for n in range(2, 20) if is_prime(n)]
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(primes, expected_primes)

        # Create a string from primes
        primes_str = ''.join(str(p) for p in primes)

        # Test string operations on prime numbers
        self.assertGreater(len(primes_str), 0)
        reversed_primes = reverse_string(primes_str)
        self.assertNotEqual(primes_str, reversed_primes)

    def test_palindromic_numbers(self):
        """Test numbers that are palindromes"""
        palindromic_nums = [11, 121, 131, 141, 151, 161, 171, 181, 191]

        for num in palindromic_nums:
            num_str = str(num)
            self.assertTrue(is_palindrome(num_str),
                          f"{num} should be a palindrome")

    def test_factorial_string_vowel_count(self):
        """Test counting vowels in factorial number words"""
        # Factorial of 6 is 720
        fact_6 = factorial(6)
        self.assertEqual(fact_6, 720)

        # Convert to word representation (simplified)
        number_words = {
            720: "seven hundred twenty",
            24: "twenty four",
            120: "one hundred twenty"
        }

        if fact_6 in number_words:
            word = number_words[fact_6]
            vowel_count = count_vowels(word)
            self.assertGreater(vowel_count, 0)

    def test_combined_mathematical_and_string_operations(self):
        """Test complex combinations of math and string operations"""
        # Calculate some values
        from calculator import add, multiply, power

        result1 = add(10, 20)
        result2 = multiply(5, 6)
        result3 = power(2, 5)

        # Combine into a string
        combined = f"{result1} {result2} {result3}"

        # Test string operations
        from string_utils import count_words, truncate
        self.assertEqual(count_words(combined), 3)

        truncated = truncate(combined, 10)
        self.assertLessEqual(len(truncated), 10)

    def test_fibonacci_palindrome_check(self):
        """Test which Fibonacci numbers are palindromes"""
        palindromic_fibs = []
        for i in range(20):
            fib = fibonacci(i)
            if is_palindrome(str(fib)):
                palindromic_fibs.append(fib)

        # Some known palindromic Fibonacci numbers
        self.assertIn(0, palindromic_fibs)
        self.assertIn(1, palindromic_fibs)
        self.assertIn(2, palindromic_fibs)
        self.assertIn(3, palindromic_fibs)
        self.assertIn(5, palindromic_fibs)
        self.assertIn(8, palindromic_fibs)

    def test_prime_factorial_comparison(self):
        """Test comparing prime checking with factorials"""
        # Some factorials are not prime (except 2! = 2)
        for n in range(3, 10):
            fact = factorial(n)
            # All factorials > 2 are not prime (divisible by smaller numbers)
            self.assertFalse(is_prime(fact),
                           f"Factorial of {n} = {fact} should not be prime")

    def test_string_transformation_pipeline(self):
        """Test a pipeline of string transformations"""
        from string_utils import remove_duplicates

        original = "hello world programming"

        # Apply transformations
        capitalized = capitalize_words(original)
        reversed_text = reverse_string(capitalized)
        no_duplicates = remove_duplicates(reversed_text)

        # Verify transformations
        self.assertNotEqual(original, capitalized)
        self.assertNotEqual(capitalized, reversed_text)
        self.assertLessEqual(len(no_duplicates), len(reversed_text))


class TestEdgeCasesIntegration(unittest.TestCase):
    """Integration tests focusing on edge cases"""

    def test_zero_factorial_string_operations(self):
        """Test factorial of 0 with string operations"""
        result = factorial(0)
        self.assertEqual(result, 1)

        result_str = str(result)
        self.assertTrue(is_palindrome(result_str))
        self.assertEqual(reverse_string(result_str), "1")

    def test_empty_string_with_math_results(self):
        """Test empty strings don't break when combined with math"""
        from calculator import add
        from string_utils import count_words, count_vowels

        result = add(5, 5)
        empty = ""
        combined = f"{result}{empty}"

        self.assertEqual(combined, "10")
        self.assertGreater(count_words(combined), 0)

    def test_large_numbers_string_representation(self):
        """Test large number calculations and string operations"""
        large_fact = factorial(10)
        self.assertEqual(large_fact, 3628800)

        large_str = str(large_fact)
        reversed_large = reverse_string(large_str)

        # Verify it's not a palindrome
        self.assertNotEqual(large_str, reversed_large)


if __name__ == '__main__':
    unittest.main()

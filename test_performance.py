"""
Performance and stress tests
"""
import unittest
import time
from calculator import (
    add, multiply, factorial, fibonacci, is_prime
)
from string_utils import (
    reverse_string, is_palindrome, remove_duplicates,
    count_vowels, count_words
)


class TestPerformance(unittest.TestCase):
    """Performance tests to ensure functions handle large inputs"""

    def test_factorial_performance(self):
        """Test factorial with moderately large numbers completes quickly"""
        start = time.time()
        result = factorial(100)
        elapsed = time.time() - start

        # Should complete in less than 1 second
        self.assertLess(elapsed, 1.0)
        # Verify it's a large number
        self.assertGreater(result, 10**100)

    def test_fibonacci_performance(self):
        """Test Fibonacci calculation performance"""
        start = time.time()
        result = fibonacci(100)
        elapsed = time.time() - start

        # Should complete reasonably fast
        self.assertLess(elapsed, 1.0)
        self.assertGreater(result, 0)

    def test_is_prime_performance_large_prime(self):
        """Test prime checking with larger numbers"""
        start = time.time()
        # Test with a known large prime
        result = is_prime(104729)  # This is a prime
        elapsed = time.time() - start

        self.assertTrue(result)
        self.assertLess(elapsed, 1.0)

    def test_is_prime_performance_large_composite(self):
        """Test prime checking with large composite numbers"""
        start = time.time()
        result = is_prime(104730)  # Not a prime
        elapsed = time.time() - start

        self.assertFalse(result)
        self.assertLess(elapsed, 1.0)

    def test_reverse_string_large(self):
        """Test reversing very large strings"""
        large_string = "abc" * 10000  # 30,000 characters
        start = time.time()
        result = reverse_string(large_string)
        elapsed = time.time() - start

        self.assertEqual(len(result), len(large_string))
        self.assertLess(elapsed, 1.0)

    def test_palindrome_large_string(self):
        """Test palindrome check with large strings"""
        large_pal = "a" * 5000 + "b" + "a" * 5000
        start = time.time()
        result = is_palindrome(large_pal)
        elapsed = time.time() - start

        self.assertTrue(result)
        self.assertLess(elapsed, 1.0)

    def test_remove_duplicates_many_duplicates(self):
        """Test removing duplicates from string with many duplicates"""
        input_str = "abcdefghij" * 1000  # 10,000 characters
        start = time.time()
        result = remove_duplicates(input_str)
        elapsed = time.time() - start

        self.assertEqual(result, "abcdefghij")
        self.assertLess(elapsed, 1.0)

    def test_count_vowels_large_text(self):
        """Test vowel counting in large text"""
        large_text = "hello world " * 1000
        start = time.time()
        result = count_vowels(large_text)
        elapsed = time.time() - start

        self.assertGreater(result, 0)
        self.assertLess(elapsed, 1.0)

    def test_count_words_large_text(self):
        """Test word counting in large text"""
        large_text = "one two three four five " * 1000
        start = time.time()
        result = count_words(large_text)
        elapsed = time.time() - start

        self.assertEqual(result, 5000)
        self.assertLess(elapsed, 1.0)


class TestStressTests(unittest.TestCase):
    """Stress tests with extreme inputs"""

    def test_massive_addition(self):
        """Test addition with extremely large numbers"""
        huge1 = 10**1000
        huge2 = 10**1000
        result = add(huge1, huge2)
        self.assertGreater(result, huge1)
        self.assertGreater(result, huge2)

    def test_massive_multiplication(self):
        """Test multiplication with very large numbers"""
        big1 = 10**100
        big2 = 10**100
        result = multiply(big1, big2)
        self.assertEqual(result, 10**200)

    def test_fibonacci_sequence_generation(self):
        """Test generating multiple Fibonacci numbers"""
        results = [fibonacci(i) for i in range(50)]
        self.assertEqual(len(results), 50)
        # Verify sequence property
        for i in range(2, 50):
            self.assertEqual(results[i], results[i-1] + results[i-2])

    def test_prime_checking_batch(self):
        """Test checking primality for many numbers"""
        primes_found = [n for n in range(2, 100) if is_prime(n)]
        # Known primes under 100
        expected_count = 25  # There are 25 primes less than 100
        self.assertEqual(len(primes_found), expected_count)

    def test_factorial_consistency(self):
        """Test factorial consistency: n! = n * (n-1)!"""
        for n in range(2, 20):
            self.assertEqual(factorial(n), n * factorial(n - 1))

    def test_string_operations_batch(self):
        """Test string operations on multiple inputs"""
        test_strings = [
            "hello", "world", "python", "testing",
            "palindrome", "racecar", "level", "test"
        ]

        for s in test_strings:
            # All operations should complete without errors
            reverse_string(s)
            is_palindrome(s)
            count_vowels(s)
            count_words(s)
            remove_duplicates(s)

        # If we get here, all operations succeeded
        self.assertTrue(True)

    def test_nested_operations(self):
        """Test nested mathematical operations"""
        # ((2^3) + 5) * 4
        from calculator import power
        result = multiply(add(power(2, 3), 5), 4)
        expected = (8 + 5) * 4
        self.assertEqual(result, expected)

    def test_repeated_string_transformations(self):
        """Test applying string transformations repeatedly"""
        text = "Hello World"
        # Apply reverse twice should give original
        result = reverse_string(reverse_string(text))
        self.assertEqual(result, text)

    def test_very_long_word_string(self):
        """Test with single very long 'word'"""
        long_word = "a" * 100000
        self.assertEqual(count_words(long_word), 1)
        self.assertEqual(count_vowels(long_word), 100000)

    def test_many_small_words(self):
        """Test with many small words"""
        many_words = " ".join(["hi"] * 10000)
        self.assertEqual(count_words(many_words), 10000)


class TestCombinedOperations(unittest.TestCase):
    """Test complex combinations of operations"""

    def test_calculate_and_analyze(self):
        """Test calculating values and analyzing them as strings"""
        from calculator import power, subtract
        from string_utils import capitalize_words

        # Calculate something
        result = subtract(power(10, 3), multiply(50, 2))
        self.assertEqual(result, 900)

        # Convert to string and analyze
        result_str = str(result)
        self.assertEqual(len(result_str), 3)

    def test_fibonacci_prime_intersection(self):
        """Test finding Fibonacci numbers that are also prime"""
        fib_primes = []
        for i in range(20):
            fib = fibonacci(i)
            if is_prime(fib):
                fib_primes.append(fib)

        # Some known Fibonacci primes
        self.assertIn(2, fib_primes)
        self.assertIn(3, fib_primes)
        self.assertIn(5, fib_primes)
        self.assertIn(13, fib_primes)

    def test_factorial_digits_analysis(self):
        """Test analyzing factorial results as strings"""
        fact_10 = factorial(10)
        fact_str = str(fact_10)

        # Count digits
        digit_count = len(fact_str)
        self.assertGreater(digit_count, 0)

        # Count vowels in the string representation
        vowels_in_number = count_vowels(fact_str)
        # Number strings don't contain vowels
        self.assertEqual(vowels_in_number, 0)

    def test_mathematical_identities(self):
        """Test mathematical identities"""
        # a * (b + c) = a*b + a*c (distributive property)
        a, b, c = 7, 3, 5
        left = multiply(a, add(b, c))
        right = add(multiply(a, b), multiply(a, c))
        self.assertEqual(left, right)

    def test_string_transformation_chain(self):
        """Test chain of string transformations"""
        original = "Python Programming Language"

        # Apply transformations
        from string_utils import capitalize_words
        step1 = capitalize_words(original)
        step2 = reverse_string(step1)
        step3 = reverse_string(step2)  # Should restore capitalization

        # After double reverse, should get back capitalized version
        self.assertEqual(step3, step1)


if __name__ == '__main__':
    unittest.main()

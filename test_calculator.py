"""
Unit tests for calculator module
"""
import unittest
from calculator import (
    add, subtract, multiply, divide, power,
    is_even, is_prime, factorial, fibonacci
)


class TestBasicOperations(unittest.TestCase):
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(0, 5), 5)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(10, -5), 5)

    def test_add_floats(self):
        """Test addition with floating point numbers"""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(20, 8), 12)
        self.assertEqual(subtract(5, 5), 0)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers"""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(-10, 5), -15)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(7, 0), 0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers"""
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-5, -6), 30)
        self.assertEqual(multiply(0, -10), 0)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)
        self.assertAlmostEqual(divide(10, 3), 3.333333, places=5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_power_positive_exponent(self):
        """Test power with positive exponent"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)

    def test_power_negative_exponent(self):
        """Test power with negative exponent"""
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(10, -2), 0.01)

    def test_power_zero_base(self):
        """Test power with zero base"""
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)


class TestNumberProperties(unittest.TestCase):
    """Test functions that check number properties"""

    def test_is_even_with_even_numbers(self):
        """Test is_even with even numbers"""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertTrue(is_even(100))

    def test_is_even_with_odd_numbers(self):
        """Test is_even with odd numbers"""
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-7))
        self.assertFalse(is_even(99))

    def test_is_prime_with_primes(self):
        """Test is_prime with prime numbers"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(97))

    def test_is_prime_with_non_primes(self):
        """Test is_prime with non-prime numbers"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))

    def test_is_prime_with_negative_numbers(self):
        """Test is_prime with negative numbers"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-5))


class TestFactorial(unittest.TestCase):
    """Test factorial function"""

    def test_factorial_base_cases(self):
        """Test factorial base cases"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_small_numbers(self):
        """Test factorial with small numbers"""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_larger_numbers(self):
        """Test factorial with larger numbers"""
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(12), 479001600)

    def test_factorial_negative_number(self):
        """Test factorial with negative number raises ValueError"""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers")

        with self.assertRaises(ValueError):
            factorial(-10)


class TestFibonacci(unittest.TestCase):
    """Test Fibonacci function"""

    def test_fibonacci_base_cases(self):
        """Test Fibonacci base cases"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        """Test Fibonacci with small numbers"""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_larger_numbers(self):
        """Test Fibonacci with larger numbers"""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_negative_index(self):
        """Test Fibonacci with negative index raises ValueError"""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Fibonacci is not defined for negative indices")

        with self.assertRaises(ValueError):
            fibonacci(-10)


if __name__ == '__main__':
    unittest.main()

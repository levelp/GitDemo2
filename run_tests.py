#!/usr/bin/env python3
"""
Test runner script that executes all tests and displays results
"""
import unittest
import sys


def run_all_tests():
    """Discover and run all tests"""
    # Create a test loader
    loader = unittest.TestLoader()

    # Discover all tests in the current directory
    suite = loader.discover('.', pattern='test_*.py')

    # Run the tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)

    # Return exit code based on results
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_all_tests())

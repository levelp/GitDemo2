# Test Suite Documentation

This repository contains **171 comprehensive tests** achieving **100% code coverage** for calculator and string utility modules.

## Test Structure

### Unit Tests

1. **test_calculator.py** - Core calculator functionality tests (26 tests)
   - TestBasicOperations: Tests for add, subtract, multiply, divide, power
   - TestNumberProperties: Tests for is_even, is_prime
   - TestFactorial: Tests for factorial function
   - TestFibonacci: Tests for Fibonacci sequence generation

2. **test_string_utils.py** - String utilities tests (50 tests)
   - TestReverseString: Tests for string reversal
   - TestIsPalindrome: Tests for palindrome detection
   - TestCountVowels: Tests for vowel counting
   - TestCapitalizeWords: Tests for word capitalization
   - TestRemoveDuplicates: Tests for duplicate character removal
   - TestCountWords: Tests for word counting
   - TestTruncate: Tests for string truncation

3. **test_integration.py** - Integration tests (15 tests)
   - TestIntegration: Tests combining calculator and string operations
   - TestEdgeCasesIntegration: Edge case integration tests

4. **test_edge_cases.py** - Edge cases and boundary values (44 tests)
   - TestCalculatorEdgeCases: Large numbers, floating point, boundaries
   - TestStringUtilsEdgeCases: Unicode, long strings, special characters
   - TestBoundaryValues: Boundary condition testing
   - TestTypeConsistency: Return type validation

5. **test_performance.py** - Performance and stress tests (26 tests)
   - TestPerformance: Performance benchmarks for large inputs
   - TestStressTests: Extreme input testing
   - TestCombinedOperations: Complex operation combinations

6. **test_error_handling.py** - Error handling and validation (30 tests)
   - TestErrorHandling: Exception testing and error messages
   - TestInputValidation: Input validation and edge cases
   - TestDataTableTests: Data-driven parameterized tests

## Running Tests

### Run all tests:
```bash
python run_tests.py
```

### Run specific test file:
```bash
python -m unittest test_calculator.py
python -m unittest test_string_utils.py
python -m unittest test_integration.py
```

### Run specific test class:
```bash
python -m unittest test_calculator.TestBasicOperations
```

### Run specific test method:
```bash
python -m unittest test_calculator.TestBasicOperations.test_add_positive_numbers
```

### Run with verbose output:
```bash
python -m unittest -v test_calculator.py
```

### Run tests with coverage:
```bash
coverage run -m unittest discover -s . -p 'test_*.py'
coverage report -m calculator.py string_utils.py
```

### Run tests with branch coverage:
```bash
coverage run --branch -m unittest discover -s . -p 'test_*.py'
coverage report --include="calculator.py,string_utils.py"
```

## Test Coverage

**100% Code Coverage Achieved!**
- **100% Statement Coverage** (69/69 statements)
- **100% Branch Coverage** (32/32 branches)

The test suite includes:
- **171 total tests** with comprehensive coverage
- **Unit tests** for individual function behavior
- **Integration tests** for module interactions
- **Edge case tests** for boundary conditions
- **Performance tests** for large inputs
- **Error handling tests** for exception scenarios
- **Data-driven tests** with parameterized inputs

### Calculator Module Coverage (calculator.py):
- Basic arithmetic operations (add, subtract, multiply, divide)
- Power operations with various exponents
- Number property checks (is_even, is_prime)
- Mathematical sequences (factorial, Fibonacci)
- Error handling (division by zero, negative factorials/indices)
- Edge cases (large numbers, floating point, zero values)

### String Utils Module Coverage (string_utils.py):
- String manipulation (reverse, truncate, remove_duplicates)
- String analysis (is_palindrome, count_vowels, count_words)
- String transformation (capitalize_words)
- Edge cases (empty strings, single characters, unicode)
- Special character handling

## Test Statistics

**Total: 171 tests** passing
- test_calculator.py: 26 tests
- test_string_utils.py: 50 tests
- test_integration.py: 15 tests
- test_edge_cases.py: 44 tests
- test_performance.py: 26 tests
- test_error_handling.py: 30 tests

All tests use Python's built-in `unittest` framework.
Coverage analysis uses the `coverage` package (see requirements.txt).

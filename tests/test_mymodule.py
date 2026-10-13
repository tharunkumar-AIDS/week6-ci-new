"""
test_mymodule.py - Automated test suite (unittest)
TDD: tests written first, then module implemented.
Run: python -m unittest test_mymodule -v  OR  pytest test_mymodule.py -v
Covers: normal, edge, error cases for all 13 functions.
"""

import unittest
from src.mymodule import (
    add, subtract, multiply, divide,
    factorial, is_prime, fibonacci, find_average,
    reverse_string, is_palindrome, count_vowels,
    capitalize_words, parse_marks
)


class TestMathOps(unittest.TestCase):
    def test_add_normal(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(2.5, 2.5), 5.0)

    def test_add_error(self):
        with self.assertRaises(TypeError):
            add("2", 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_type_error(self):
        with self.assertRaises(TypeError):
            divide("10", 2)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_errors(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(-7))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_find_average(self):
        self.assertEqual(find_average([10, 20, 30]), 20)
        self.assertEqual(find_average([]), 0.0)
        self.assertEqual(find_average([10, "bad", 20]), 15)  # skips bad
        with self.assertRaises(TypeError):
            find_average("notalist")


class TestStrings(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_palindrome(self):
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("nurses run"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome(""))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_capitalize(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("  python   rocks  "), "Python Rocks")
        self.assertEqual(capitalize_words(""), "")


class TestParsing(unittest.TestCase):
    def test_parse_normal(self):
        self.assertEqual(parse_marks("80,90,70"), [80.0, 90.0, 70.0])

    def test_parse_spaces_invalid(self):
        self.assertEqual(parse_marks("80, abc, 200, 70"), [80.0, 70.0])

    def test_parse_empty(self):
        self.assertEqual(parse_marks(""), [])
        self.assertEqual(parse_marks("   "), [])

    def test_parse_type_error(self):
        with self.assertRaises(TypeError):
            parse_marks(123)


class TestIntegration(unittest.TestCase):
    """Integration: parse -> average -> grade logic together."""
    def test_full_flow(self):
        marks = parse_marks("80,90,100")
        avg = find_average(marks)
        self.assertAlmostEqual(avg, 90.0)
        # grade boundary check
        grade = "A" if avg >= 90 else "B"
        self.assertEqual(grade, "A")

    def test_empty_flow(self):
        marks = parse_marks("")
        avg = find_average(marks)
        self.assertEqual(avg, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

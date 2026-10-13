"""
mymodule.py - Mini utility library for Week 3 TDD Task
Designed to be easy to test: pure functions, no I/O, clear errors.
Covers: math ops, string manipulation, data parsing.
"""

# ---------- Math Operations ----------


def add(a, b):
    """Return a+b. Works for int/float."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("add() needs numbers")
    return a + b


def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("subtract() needs numbers")
    return a - b


def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("multiply() needs numbers")
    return a * b


def divide(a, b):
    """Divide a/b. Raises ZeroDivisionError on b==0, TypeError on non-numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("divide() needs numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def factorial(n):
    """Factorial of non-negative int. Raises ValueError/TypeError otherwise."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("factorial() needs int")
    if n < 0:
        raise ValueError("factorial() not defined for negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    """Return first n fibonacci numbers as list. n>=0."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("fibonacci() needs int")
    if n < 0:
        raise ValueError("fibonacci() needs n>=0")
    if n == 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def find_average(numbers):
    """Average of list. Returns 0.0 for empty. Skips non-numbers."""
    if not isinstance(numbers, list):
        raise TypeError("find_average() needs list")
    cleaned = [x for x in numbers if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not cleaned:
        return 0.0
    return sum(cleaned) / len(cleaned)


# ---------- String Manipulation ----------

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("reverse_string() needs str")
    return s[::-1]


def is_palindrome(s):
    """Case-insensitive, ignores spaces."""
    if not isinstance(s, str):
        raise TypeError("is_palindrome() needs str")
    clean = "".join(s.lower().split())
    return clean == clean[::-1] and len(clean) > 0


def count_vowels(s):
    if not isinstance(s, str):
        raise TypeError("count_vowels() needs str")
    return sum(1 for ch in s.lower() if ch in "aeiou")


def capitalize_words(s):
    """Capitalize each word, strip extra spaces."""
    if not isinstance(s, str):
        raise TypeError("capitalize_words() needs str")
    return " ".join(word.capitalize() for word in s.strip().split() if word)


# ---------- Data Parsing ----------

def parse_marks(marks_str):
    """Parse '80,90,70' -> [80.0,90.0,70.0]. Skips invalid/out-of-range."""
    if not isinstance(marks_str, str):
        raise TypeError("parse_marks() needs str")
    if not marks_str.strip():
        return []
    result = []
    for part in marks_str.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            val = float(part)
            if 0 <= val <= 100:
                result.append(val)
        except ValueError:
            continue
    return result

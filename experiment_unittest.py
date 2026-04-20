import unittest


def factorial(n):
    if n < 0:
        return "Invalid"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_palindrome(s):
    return s == s[::-1]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sort_list(lst):
    return sorted(lst)


def fibonacci(n):
    if n < 0:
        return "Invalid"
    if n == 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


class TestFactorial(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_negative(self):
        self.assertEqual(factorial(-3), "Invalid")


class TestPalindrome(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_palindrome("abba"))

    def test_odd(self):
        self.assertTrue(is_palindrome("madam"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_digits(self):
        self.assertTrue(is_palindrome("12321"))

    def test_special_chars(self):
        self.assertTrue(is_palindrome("a@a"))


class TestPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(7))

    def test_non_prime(self):
        self.assertFalse(is_prime(4))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_negative(self):
        self.assertFalse(is_prime(-5))


class TestSort(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(sort_list([]), [])

    def test_duplicates(self):
        self.assertEqual(sort_list([5, 5, 2, 2]), [2, 2, 5, 5])

    def test_single(self):
        self.assertEqual(sort_list([10]), [10])


class TestFibonacci(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_zero(self):
        self.assertEqual(fibonacci(0), [])

    def test_one(self):
        self.assertEqual(fibonacci(1), [0])

    def test_negative(self):
        self.assertEqual(fibonacci(-3), "Invalid")


if __name__ == "__main__":
    unittest.main()

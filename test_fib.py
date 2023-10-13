import unittest
from fib import fib


class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fib(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fib(1), 1)

    def test_fibonacci_5(self):
        self.assertEqual(fib(5), 5)

    def test_fibonacci_10(self):
        self.assertEqual(fib(10), 55)

    def test_fibonacci_20(self):
        self.assertEqual(fib(20), 6765)


if __name__ == "__main__":
    unittest.main()

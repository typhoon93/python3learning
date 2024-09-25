import unittest


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 4), 7, "Should be 7")

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0, "Should be 0")
        self.assertEqual(add_numbers(0, 5), 5, "Should be 5")
        self.assertEqual(add_numbers(5, 0), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -1), -2, "Should be -2")
        self.assertEqual(add_numbers(-1, 2), 1, "Should be 1")

    def test_add_large_numbers(self):
        self.assertEqual(add_numbers(1000000, 1000000), 2000000, "Should be 2000000")

    def test_add_non_integer(self):
        self.assertEqual(add_numbers(1.5, 2.3), 3.8, "Should be 3.8")
        with self.assertRaises(TypeError):
            add_numbers("one", 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
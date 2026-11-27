#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        """Ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Unordered list"""
        self.assertEqual(max_integer([1, 20, 3, 4]), 20)

    def test_max_at_beginning(self):
        """Max at the beginning"""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        """Max in the middle"""
        self.assertEqual(max_integer([1, 2, 30, 4, 5]), 30)

    def test_empty_list(self):
        """Empty list"""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """No argument"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """List with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """Positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_duplicates(self):
        """Duplicate max values"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """Integers and floats mixed"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """A string is iterable"""
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        """List of strings"""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_of_lists(self):
        """List of lists"""
        self.assertEqual(max_integer([[1], [3], [2]]), [3])

    def test_mixed_types(self):
        """Mixed types raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none(self):
        """None raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_argument(self):
        """An integer raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()

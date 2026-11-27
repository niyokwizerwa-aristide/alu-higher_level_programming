#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the saved file."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_two_args(self):
        """Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 0, 0, 1))

    def test_three_args(self):
        """Rectangle(1, 2, 3)."""
        self.assertEqual(Rectangle(1, 2, 3).x, 3)

    def test_four_args(self):
        """Rectangle(1, 2, 3, 4)."""
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)

    def test_five_args(self):
        """Rectangle(1, 2, 3, 4, 5)."""
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_string_width(self):
        """Rectangle("1", 2)."""
        with self.assertRaises(TypeError) as c:
            Rectangle("1", 2)
        self.assertEqual(str(c.exception), "width must be an integer")

    def test_string_height(self):
        """Rectangle(1, "2")."""
        with self.assertRaises(TypeError) as c:
            Rectangle(1, "2")
        self.assertEqual(str(c.exception), "height must be an integer")

    def test_string_x(self):
        """Rectangle(1, 2, "3")."""
        with self.assertRaises(TypeError) as c:
            Rectangle(1, 2, "3")
        self.assertEqual(str(c.exception), "x must be an integer")

    def test_string_y(self):
        """Rectangle(1, 2, 3, "4")."""
        with self.assertRaises(TypeError) as c:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(c.exception), "y must be an integer")

    def test_negative_width(self):
        """Rectangle(-1, 2)."""
        with self.assertRaises(ValueError) as c:
            Rectangle(-1, 2)
        self.assertEqual(str(c.exception), "width must be > 0")

    def test_negative_height(self):
        """Rectangle(1, -2)."""
        with self.assertRaises(ValueError) as c:
            Rectangle(1, -2)
        self.assertEqual(str(c.exception), "height must be > 0")

    def test_zero_width(self):
        """Rectangle(0, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Rectangle(1, 0)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x(self):
        """Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError) as c:
            Rectangle(1, 2, -3)
        self.assertEqual(str(c.exception), "x must be >= 0")

    def test_negative_y(self):
        """Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError) as c:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(c.exception), "y must be >= 0")

    def test_area(self):
        """area()."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        """__str__()."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        """to_dictionary()."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(),
                         {'id': 5, 'width': 1, 'height': 2,
                          'x': 3, 'y': 4})

    def test_update_none(self):
        """update()."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_args(self):
        """update with positional arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89, 10, 20, 30, 40)
        self.assertEqual(r.to_dictionary(),
                         {'id': 89, 'width': 10, 'height': 20,
                          'x': 30, 'y': 40})

    def test_update_kwargs(self):
        """update with keyword arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(**{'id': 89, 'width': 7, 'x': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 2/4 - 7/2")

    def test_create(self):
        """create(**dictionary)."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
                                'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_none(self):
        """save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_one(self):
        """save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as f:
            self.assertEqual(len(f.read()) > 2, True)

    def test_load_missing(self):
        """load_from_file when the file doesn't exist."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_existing(self):
        """load_from_file when the file exists."""
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(loaded[0]), "[Rectangle] (5) 3/4 - 1/2")


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for the Square class."""
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the saved file."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_one_arg(self):
        """Square(1)."""
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 0, 0, 1))

    def test_two_args(self):
        """Square(1, 2)."""
        self.assertEqual(Square(1, 2).x, 2)

    def test_three_args(self):
        """Square(1, 2, 3)."""
        self.assertEqual(Square(1, 2, 3).y, 3)

    def test_four_args(self):
        """Square(1, 2, 3, 4)."""
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_string_size(self):
        """Square("1")."""
        with self.assertRaises(TypeError) as c:
            Square("1")
        self.assertEqual(str(c.exception), "width must be an integer")

    def test_string_x(self):
        """Square(1, "2")."""
        with self.assertRaises(TypeError) as c:
            Square(1, "2")
        self.assertEqual(str(c.exception), "x must be an integer")

    def test_string_y(self):
        """Square(1, 2, "3")."""
        with self.assertRaises(TypeError) as c:
            Square(1, 2, "3")
        self.assertEqual(str(c.exception), "y must be an integer")

    def test_negative_size(self):
        """Square(-1)."""
        with self.assertRaises(ValueError) as c:
            Square(-1)
        self.assertEqual(str(c.exception), "width must be > 0")

    def test_negative_x(self):
        """Square(1, -2)."""
        with self.assertRaises(ValueError) as c:
            Square(1, -2)
        self.assertEqual(str(c.exception), "x must be >= 0")

    def test_negative_y(self):
        """Square(1, 2, -3)."""
        with self.assertRaises(ValueError) as c:
            Square(1, 2, -3)
        self.assertEqual(str(c.exception), "y must be >= 0")

    def test_zero_size(self):
        """Square(0)."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """__str__()."""
        self.assertEqual(str(Square(5, 2, 1, 12)),
                         "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        """to_dictionary()."""
        self.assertEqual(Square(1, 2, 3, 4).to_dictionary(),
                         {'id': 4, 'x': 2, 'size': 1, 'y': 3})

    def test_update_none(self):
        """update()."""
        s = Square(1, 2, 3, 4)
        s.update()
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_update_id(self):
        """update(89)."""
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_size(self):
        """update(89, 1)."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_x(self):
        """update(89, 1, 2)."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_y(self):
        """update(89, 1, 2, 3)."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_kwargs_id(self):
        """update(**{'id': 89})."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_size(self):
        """update(**{'id': 89, 'size': 1})."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_x(self):
        """update(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_y(self):
        """update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_id(self):
        """create(**{'id': 89})."""
        self.assertEqual(Square.create(**{'id': 89}).id, 89)

    def test_create_size(self):
        """create with id and size."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_x(self):
        """create with id, size and x."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_y(self):
        """create with id, size, x and y."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_save_none(self):
        """save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_one(self):
        """save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertEqual(len(f.read()) > 2, True)

    def test_load_missing(self):
        """load_from_file when the file doesn't exist."""
        self.assertEqual(Square.load_from_file(), [])

    def test_load_existing(self):
        """load_from_file when the file exists."""
        Square.save_to_file([Square(1, 2, 3, 4)])
        loaded = Square.load_from_file()
        self.assertEqual(str(loaded[0]), "[Square] (4) 2/3 - 1")


if __name__ == '__main__':
    unittest.main()

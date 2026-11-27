#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_valid_init(self):
        """Test valid initialization."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)

    def test_type_errors(self):
        """Test TypeError for non-integer attributes."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        """Test ValueError for invalid integer ranges."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area calculation."""
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_str(self):
        """Test string representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        """Test display() without x and y."""
        r = Rectangle(2, 3)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n##\n")

    def test_display_no_y(self):
        """Test display() with x but without y."""
        r = Rectangle(2, 3, 2)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "  ##\n  ##\n  ##\n")

    def test_display_xy(self):
        """Test display() with both x and y."""
        r = Rectangle(2, 3, 2, 2)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary output."""
        r = Rectangle(10, 2, 1, 9, 7)
        expected = {"id": 7, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_args(self):
        """Test update with *args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1, width=2, x=3, y=4, id=99)
        self.assertEqual(str(r), "[Rectangle] (99) 3/4 - 2/1")

    def test_create(self):
        """Test create class method."""
        r = Rectangle.create(id=89, width=2, height=3, x=1, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/4 - 2/3")

    def test_save_and_load_file(self):
        """Test save_to_file and load_from_file."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])

        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(r1))
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()

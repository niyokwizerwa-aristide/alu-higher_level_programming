#!/usr/bin/python3
"""Unittest for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for Base."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Base() assigns an id automatically."""
        self.assertEqual(Base().id, 1)

    def test_auto_id_plus_one(self):
        """Base() assigns the previous id + 1."""
        Base()
        self.assertEqual(Base().id, 2)

    def test_id_given(self):
        """Base(89) saves the id passed."""
        self.assertEqual(Base(89).id, 89)

    def test_to_json_none(self):
        """to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        """to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_dict(self):
        """to_json_string with one dictionary."""
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         '[{"id": 12}]')

    def test_to_json_type(self):
        """to_json_string returns a string."""
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_none(self):
        """from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_dict(self):
        """from_json_string with one dictionary."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{'id': 89}])

    def test_load_missing_file(self):
        """load_from_file when the file doesn't exist."""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        self.assertEqual(Base.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()

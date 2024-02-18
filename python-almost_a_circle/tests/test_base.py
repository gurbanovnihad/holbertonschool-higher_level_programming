#!/usr/bin/python3

"""
    Tests for Almost A circle module - Base Class
"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def test_id(self):
        # None
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base(None)
        self.assertEqual(b1.id, 2)

        # Positive integer
        b2 = Base(4)
        self.assertEqual(b2.id, 4)

        b2 = Base(9)
        self.assertEqual(b2.id, 9)

        # Negative integer
        b3 = Base(-3)
        self.assertEqual(b3.id, -3)

        b3 = Base(-7)
        self.assertEqual(b3.id, -7)

        # String
        b4  = Base("Checker checker")
        self.assertEqual(b4.id, "Checker checker")

        b4 = Base("String testing.")
        self.assertEqual(b4.id, "String testing.")

    def test_json_converters(self):
        """
            Tests to_json_string method
        """
        # None
        json_string_1 = Base.to_json_string(None)
        self.assertEqual(json_string_1, "[]")

        # Empty list
        json_string_2 = Base.to_json_string([])
        self.assertEqual(json_string_2, "[]")

        # Ordinary Dictionary
        json_string_3 = Base.to_json_string([{"id": 1}])
        self.assertEqual(json_string_3, '[{"id": 1}]')

        """
            Tests from_json_string method
        """
        # None
        list_1 = Base.from_json_string(None)
        self.assertEqual(list_1, [])

        # Empty list string
        list_2 = Base.from_json_string("[]")
        self.assertEqual(list_2, [])

        # Ordinary json string
        list_3 = Base.from_json_string('[{"id": 4}]')
        self.assertEqual(list_3, [{"id": 4}])

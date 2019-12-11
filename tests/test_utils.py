# -*- coding: utf-8 -*-

"""This file contains the test functions for charly."""

import unittest

from charly import add


class TestAdd(unittest.TestCase):
    """Class for the tests."""

    def test_identitiy(self):
        """This test makes sure that addition to zero doesn't do anything."""
        a = 1
        result = add(a, 0)
        self.assertEqual(a, result)

    def rest_add_negation(self):
        """Test if the add functions."""
        a, b = -1, 1
        expected = a+b
        actual = add(a, b)
        self.assertEqual(expected, actual)

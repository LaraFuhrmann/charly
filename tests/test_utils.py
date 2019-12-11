import unittest
from charly import add


class TestAdd(unittest.TestCase):

    def test_identitiy(self):
        """This test makes sure that addition to zero doesn't do anything"""
        a = 1
        result = add(a, 0)
        self.assertEqual(a,result)

    def rest_add_negation(self):
        a,b = -1, 1
        expected = a+b
        actual = add(a,b)
        self.assertEqual(expected, actual)

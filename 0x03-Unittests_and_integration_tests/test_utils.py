#!/usr/bin/env python3
""" TestAccessNestedMap class module """
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class implementation """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ method to test that the method returns what it is supposed to. """
        self.assertEqual(self.access_nested_map(nested_map, path), expected)

    def access_nested_map(self, nested_map, path):
        """ Function to access nested map """
        value = nested_map
        for key in path:
            value = value[key]
        return value


if __name__ == '__main__':
    unittest.main()

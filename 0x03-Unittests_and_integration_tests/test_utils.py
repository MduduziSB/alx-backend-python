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

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map['a']"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_err):
        """ KeyError test method """
        with self.assertRaises(KeyError) as context:
            self.access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_err)

#!/usr/bin/env python3
"""Unittest for utils.py to ensure that the access_nested_map
function works well as expected.
Also decorarte the test class with the parameterized decorator
to test multiple cases.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class to test the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_message):
        """ Test the access of nested_map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(access_nested_map, path)
        self.assertEqual(str(cm.exception), expected_message)


if __name__ == "__main__":
    unittest.main()

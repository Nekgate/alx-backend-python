#!/usr/bin/env python3
"""Unittest for utils.py to ensure that the access_nested_map
function works well as expected.
Also decorarte the test class with the parameterized decorator
to test multiple cases.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock 
from utils import access_nested_map, get_json


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
        """ Test the access of nested_map.
        """

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(expected_key))


class TestGetJson(unittest.TestCase):
    """ Class to test the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test that get_json returns the expected
        result with mocked requests.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Check that requests.get was called once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Check that the result matches the test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()

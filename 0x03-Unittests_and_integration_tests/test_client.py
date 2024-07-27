#!/usr/bin/env python3
"""Unittest for client.py to ensure that the
GithubOrgClient class works as expected.
Also uses decorators to parametrize
the test and patch external calls.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Set up the mock for get_json to return a specific payload
        mock_get_json.return_value = expected_payload

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Check that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Check that the org method returns the expected result
        self.assertEqual(result, expected_payload)


if __name__ == "__main__":
    unittest.main()

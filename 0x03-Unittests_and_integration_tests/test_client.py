#!/usr/bin/env python3
"""Unittest for client.py to ensure that the
GithubOrgClient class works as expected.
Also uses decorators to parametrize
the test and patch external calls.
class behaves as expected. Specifically, testing
the _public_repos_url property.
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the GithubOrgClient class."""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the
        expected URL based on the mocked org property.
        """
        # Define a known payload for the org property
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Create an instance of GithubOrgClient with a known org_name
        client = GithubOrgClient("google")

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Define the expected URL
        expected_url = "https://api.github.com/orgs/google/repos"

        # Check that _public_repos_url returns the expected URL
        self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()

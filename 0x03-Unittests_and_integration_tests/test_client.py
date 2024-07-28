#!/usr/bin/env python3
"""Unittest for client.py to ensure that the
GithubOrgClient class behaves as expected.
Specifically, testing the public_repos method.
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the GithubOrgClient class."""

    @patch('utils.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self,
                          mock_public_repos_url, mock_get_json):
        """Test that public_repos returns the expected
        repos list and that mocks are called correctly.
        """

        # Define a known payload for get_json
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        # Define a known URL for _public_repos_url
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

        # Set up the mock for get_json to return the test payload
        mock_get_json.return_value = test_payload

        # Create an instance of GithubOrgClient with a known org_name
        client = GithubOrgClient("google")

        # Define the expected repos list
        expected_repos = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        # Call public_repos method
        repos = client.public_repos()

        # Check that public_repos returns the expected repos list
        self.assertEqual(repos, expected_repos)

        # Check that the _public_repos_url property was once
        mock_public_repos_url.assert_called_once()

        # Check that get_json was called exactly once with the mocked URL
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()

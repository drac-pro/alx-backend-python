#!/usr/bin/env python3
"""defines a test class to test the client module"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import (GithubOrgClient)


class TestGithubOrgClient(unittest.TestCase):
    """tests GithubOrgClient class from the client module"""
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_func):
        """test org method with different parameters"""
        mock_func.return_value = Mock(return_value=expected)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), expected)
        mock_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        """tests public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/users/google/repos'}
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             'https://api.github.com/users/google/repos')

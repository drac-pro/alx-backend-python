#!/usr/bin/env python3
"""defines a test class to test the client module"""
import unittest
from unittest.mock import (patch, Mock, PropertyMock)
from parameterized import (parameterized, parameterized_class)
from client import GithubOrgClient
from requests import HTTPError
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """tests public_repos method"""
        test_payload = TEST_PAYLOAD[0]
        mock_get_json.return_value = test_payload[1]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload[0]['repos_url']
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                test_payload[2]
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False)
    ])
    def test_has_license(self, repo, key, expected):
        """tests has_license method"""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Intergration test of GithubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """sets up the test class before running test casses"""
        url_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload
        }

        def get_payload(url):
            if url in url_payload:
                return Mock(**{'json.return_value': url_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """stops patcher"""
        cls.get_patcher.stop()

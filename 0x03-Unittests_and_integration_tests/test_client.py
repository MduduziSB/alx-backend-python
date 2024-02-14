#!/usr/bin/env python3
"""A module for testing the client module.
"""
from unittest import TestCase, mock
from typing import Dict
from unittest.mock import MagicMock, Mock
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import unittest


class TestGithubOrgClient(TestCase):
    """ TestGithubOrgClient definition"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, moc: MagicMock) -> None:
        """test_org method implimentation"""
        moc.return_value = MagicMock(return_value=resp)
        cient_org = GithubOrgClient(org)
        self.assertEqual(client_org.org(), resp)
        url = "https://api.github.com/orgs/{}".format(org)
        moc.assert_called_once_with(url)

    def test_public_repos_url(self) -> None:
        """test_public_repos_url implimentation"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as org:
            org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """ test_public_repos method implimentation """
        expected_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = expected_payload

        # Mocking the _public_repos_url property
        with patch.object(
                'client.GithubOrgClient._public_repos_url',
                new_callable=MagicMock,
                ) as mock_public_repos_url:
            rep_url = 'https://api.github.com/orgs/example_org/repos'
            mock_public_repos_url.return_value = rep_url
            client = GithubOrgClient('example_org')
            repos = client.public_repos
            self.assertEqual(repos, expected_payload)
            url = 'https://api.github.com/orgs/example_org/repos'
            mock_get_json.assert_called_once_with(url)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests the has_license method."""
        org_client = GithubOrgClient("google")
        client_has_licence = org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """ class fixtures setup"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """ test_public_repos method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """ test_public_repos_with_license method"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down implimentation"""
        cls.get_patcher.stop()

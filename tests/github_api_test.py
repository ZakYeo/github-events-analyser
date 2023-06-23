import unittest
from unittest.mock import patch, Mock
from github_events_analyser.github_api import GitHubAPI

__author__ = "ZakYeo"
__copyright__ = "ZakYeo"
__license__ = "MIT"


class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        """
        setUp runs before each test case. Here, it's used to set up some
        common variables and a GitHubAPI instance.
        """
        self.token = 'test_token'
        self.api = GitHubAPI(self.token)
        self.username = 'test_username'
        self.repo = 'test_repo'
        self.event_type = 'PushEvent'

    @patch('github_events_analyser.github_api.requests.get')
    def test_get_user_info(self, mock_get):
        """
        Tests the get_user_info function.
        """
        # Mock the response from requests.get
        mock_resp = Mock()
        expected_result = {"login": self.username}
        mock_resp.json.return_value = expected_result
        mock_get.return_value = mock_resp

        result = self.api.get_user_info(self.username)

        # Assert that the function returns the expected result
        self.assertEqual(result, expected_result)

    @patch('github_events_analyser.github_api.requests.get')
    def test_get_user_events(self, mock_get):
        """
        Tests the get_user_events function.
        """
        # Mock the response from requests.get
        mock_resp = Mock()
        expected_result = [{'type': self.event_type}]
        mock_resp.json.return_value = expected_result
        mock_get.return_value = mock_resp

        result = self.api.get_user_events(self.username, self.event_type)

        # Assert that the function returns the expected result
        self.assertEqual(result, expected_result)

    @patch('github_events_analyser.github_api.requests.get')
    def test_get_repo_events(self, mock_get):
        """
        Tests the get_repo_events function.
        """
        # Mock the response from requests.get
        mock_resp = Mock()
        expected_result = [{'type': self.event_type}]
        mock_resp.json.return_value = expected_result
        mock_get.return_value = mock_resp

        result = self.api.get_repo_events(self.username, self.repo, self.event_type)

        # Assert that the function returns the expected result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

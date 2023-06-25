import unittest
from unittest.mock import patch, Mock
from github_events_analyser.github_api import GitHubAPI
import requests

__author__ = "ZakYeo"
__copyright__ = "ZakYeo"
__license__ = "MIT"


class TestGitHubAPI(unittest.TestCase):
    """Unit test class for GitHubAPI."""

    def setUp(self):
        """
        setUp runs before each test case. It's used to set up some
        common variables and a GitHubAPI instance for the tests.
        """
        self.token = ''  # Place your GitHub token here before running unit tests
        self.api = GitHubAPI(self.token)
        self.username = 'ZakYeo'
        self.repo = 'github-events-analyser'

    @patch('requests.get')
    def test_get_repo_events(self, mock_get):
        """
        Tests the get_repo_events method of the GitHubAPI class for a successful API request.
        """
        # Arrange: Set up the mock response for the get request
        mock_response = Mock()
        expected_json = [{'id': '123', 'type': 'PushEvent'}]
        mock_response.json.return_value = expected_json
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        github_api = GitHubAPI(self.token)

        # Act: Call the method under test
        actual = github_api.get_repo_events(self.username, self.repo)

        # Assert: Check that the get request was made correctly and the method returns correct data
        mock_get.assert_called_once_with(f'https://api.github.com/repos/{self.username}/{self.repo}/events?page=1&per_page=30',
                                         headers={'Authorization': f'token {self.token}',
                                                  'Accept': 'application/vnd.github.v3+json'})
        self.assertEqual(expected_json, actual.json())

    @patch('requests.get')
    def test_get_repo_events_http_error(self, mock_get):
        """
        Tests the get_repo_events method of the GitHubAPI class for an HTTP error.
        """
        # Arrange: Set the get request to raise an HTTPError
        mock_get.side_effect = requests.HTTPError('HTTP Error Occurred')
        github_api = GitHubAPI(self.token)

        # Act: Call the method under test
        actual = github_api.get_repo_events(self.username, self.repo)

        # Assert: Check that the method handles the error correctly
        self.assertEqual({"error": 'HTTP Error Occurred'}, actual)

    @patch('requests.get')
    def test_get_repo_events_other_error(self, mock_get):
        """
        Tests the get_repo_events method of the GitHubAPI class for a non-HTTP error.
        """
        # Arrange: Set the get request to raise a generic Exception
        mock_get.side_effect = Exception('Unexpected Error')
        github_api = GitHubAPI(self.token)

        # Act: Call the method under test
        actual = github_api.get_repo_events(self.username, self.repo)

        # Assert: Check that the method handles the error correctly
        self.assertEqual({"error": 'Unexpected Error'}, actual)


if __name__ == '__main__':
    import logging
    # Set up logging to only output critical messages
    logging.basicConfig(level=logging.CRITICAL)

    unittest.main()

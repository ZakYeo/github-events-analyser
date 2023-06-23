# github_api.py

import requests


class GitHubAPI:
    """
    A wrapper class for the GitHub API.

    Attributes:
        BASE_URL (str): The base URL for the GitHub API.
    """

    BASE_URL = 'https://api.github.com'

    def __init__(self, token):
        """
        Initializes the GitHubAPI class with an authentication token.

        Args:
            token (str): The GitHub API token.
        """
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_user_info(self, username):
        """
        Fetches information about a GitHub user.

        Args:
            username (str): The GitHub username.

        Returns:
            dict: The user's information.
        """
        response = requests.get(
            f'{self.BASE_URL}/users/{username}', headers=self.headers)
        return response.json()

    def get_user_events(self, username, event_type=None):
        """
        Fetches events associated with a GitHub user.

        Args:
            username (str): The GitHub username.
            event_type (str, optional): The type of event to fetch.

        Returns:
            list: The user's events.
        """
        response = requests.get(
            f'{self.BASE_URL}/users/{username}/events', headers=self.headers)
        events = response.json()

        # If an event type is specified, filter the events
        if event_type:
            events = [event for event in events if event['type'] == event_type]

        return events

    def get_repo_events(self, username, repo, event_type=None):
        """
        Fetch and display the latest events for a given GitHub repository
        Filter events using event_type, e.g y "PushEvent" or "PullRequestEvent"

        TODO:
            - Calculate and display statistics on the number of events per type
            - Identify the most active GitHub user based on the number of events
            - Implement error handling for API requests and display appropriate
            error messages
            - Use pagination to handle a large number of events and enable the
            retrieval of more events beyond the initial limit.
            - Implement sorting options to display events in chronological or
            reverse-chronological order.

        Args:
            username (str): The owner of the repository.
            repo (str): The repository name.
            event_type (str, optional): The type of event to fetch.

        Returns:
            list: The repository's events.
        """
        url = f'{self.BASE_URL}/repos/{username}/{repo}/events'
        response = requests.get(
            url, headers=self.headers)
        return response.json()

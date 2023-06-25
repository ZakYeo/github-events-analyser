import requests
import logging


class GitHubAPI:
    """
    A wrapper class for the GitHub API.

    Attributes:
        BASE_URL (str): The base URL for the GitHub API.
    """

    BASE_URL = 'https://api.github.com'
    EVENTS = ["CommitCommentEvent", "CreateEvent", "DeleteEvent", "ForkEvent",
              "GollumEvent", "IssueCommentEvent", "IssuesEvent", "MemberEvent",
              "PublicEvent", "PullRequestEvent", "PullRequestReviewEvent",
              "PullRequestReviewCommentEvent", "PullRequestReviewThreadEvent",
              "PushEvent", "ReleaseEvent", "SponsorshipEvent", "WatchEvent"]

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
        logging.basicConfig(level=logging.INFO)

    def get_user_info(self, username):
        """
        Fetches information about a GitHub user.

        Args:
            username (str): The GitHub username.

        Returns:
            dict: The user's information.
        """
        try:
            response = requests.get(
                f'{self.BASE_URL}/users/{username}', headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
            return {"error": str(http_err)}
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
            return {"error": str(err)}
        else:
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
        try:
            response = requests.get(
                f'{self.BASE_URL}/users/{username}/events', headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
            return {"error": str(http_err)}
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
            return {"error": str(err)}
        else:
            events = response.json()

            # If an event type is specified, filter the events
            if event_type:
                events = [event for event in events if event['type'] == event_type]

            return events

    def get_repo_events(self, username, repo, event_type=None):
        """
        Fetch and display the latest events for a given GitHub repository
        Filter events using event_type, e.g by "PushEvent" or "PullRequestEvent"

        TODO:
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
        try:
            url = f'{self.BASE_URL}/repos/{username}/{repo}/events'
            response = requests.get(
                url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
            return {"error": str(http_err)}
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
            return {"error": str(err)}
        else:
            return response

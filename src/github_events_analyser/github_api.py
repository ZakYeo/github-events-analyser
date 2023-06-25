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

    def get_repo_events(self, username, repo, per_page=30, page=1):
        """
        Fetch and display the latest events for a given GitHub repository
        Filter events using event_type, e.g by "PushEvent" or "PullRequestEvent"

        Args:
            username (str): The owner of the repository.
            repo (str): The repository name.
            event_type (str, optional): The type of event to fetch.

        Returns:
            list: The repository's events.
        """
        try:
            url = f'{self.BASE_URL}/repos/{username}/{repo}/events?page={page}&per_page={per_page}'
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

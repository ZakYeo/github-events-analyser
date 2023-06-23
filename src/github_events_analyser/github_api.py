# github_api.py

import requests


class GitHubAPI:
    BASE_URL = 'https://api.github.com'

    def __init__(self, token):
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_user_info(self, username):
        response = requests.get(
            f'{self.BASE_URL}/users/{username}', headers=self.headers)
        return response.json()

    def get_user_events(self, username, event_type=None):
        response = requests.get(
            f'{self.BASE_URL}/users/{username}/events', headers=self.headers)
        events = response.json()

        if event_type:
            events = [event for event in events if event['type'] == event_type]

        return events

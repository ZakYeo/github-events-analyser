# cli.py

import argparse
from .github_api import GitHubAPI


def user_info(args):
    api = GitHubAPI(args.token)
    user_info = api.get_user_info(args.username)
    print(user_info)


def user_events(args):
    api = GitHubAPI(args.token)
    events = api.get_user_events(args.username, args.event_type)
    print(events)


def repo_events(args):
    api = GitHubAPI(args.token)
    events = api.get_repo_events(args.username, args.repo, args.event_type)
    print(events)


def main():
    parser = argparse.ArgumentParser(description='Interact with GitHub API.')
    parser.add_argument('--token', required=True, help='Your GitHub token')
    subparsers = parser.add_subparsers()

    parser_user_info = subparsers.add_parser('user-info', help='Fetch user info')
    parser_user_info.add_argument('username', help='GitHub username to fetch info for')
    parser_user_info.set_defaults(func=user_info)

    parser_user_events = subparsers.add_parser('user-events', help='Fetch user events')
    parser_user_events.add_argument(
        'username', help='GitHub username to fetch events for')
    parser_user_events.add_argument('--event-type', help='Type of events to fetch')
    parser_user_events.set_defaults(func=user_events)

    parser_repo_events = subparsers.add_parser('repo-events', help='Fetch repo events')
    parser_repo_events.add_argument(
        'username', help='GitHub username to fetch events for')
    parser_repo_events.add_argument(
        'repo', help='GitHub repository to fetch events for')
    parser_repo_events.add_argument('--event-type', help='Type of events to fetch')
    parser_repo_events.set_defaults(func=repo_events)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

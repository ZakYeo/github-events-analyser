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
    # Create a dictionary to count the amount of events
    event_counter = {event: 0 for event in api.EVENTS}
    # Create a dictionary to tally events from users
    user_counter = {}
    total_events = 0
    response_events = api.get_repo_events(
        args.username, args.repo, args.per_page, args.page)
    json_resp = response_events.json()
    print(f"Repository Events For: {args.repo}")

    for item in json_resp:
        event_counter[item['type']] += 1
        try:
            description = item['payload']['description']
        except KeyError:
            # Description does not exist, use message instead
            # Can be multiple messages, so concatenate all
            description = ""
            for commit in item['payload']['commits']:

                description += commit["message"]
            description = description.replace("\n", " || ")
        total_events += 1
        # Add one to the tally for this user
        user = item['actor']['display_login']
        try:
            user_counter[user] += 1
        except KeyError:
            # Does not exist yet, create it
            user_counter[user] = 1

        print(
            f"""{item['type']} By {item['actor']['display_login']} at {item['created_at']} || {description}""")
    print(f"Total Events {total_events}: ", end='')
    print(', '.join([f"{k}: {v}" for k, v in event_counter.items() if v > 0]))
    try:
        most_active_user = max(user_counter, key=user_counter.get)
        print(
            f"Most Active User In This Repo: {most_active_user} at {user_counter[most_active_user]} events")
    except ValueError:
        # user_counter is empty, so cannot use max().
        pass


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
    parser_repo_events.add_argument(
        '--per-page', help='Number of events to display per page (max 100)')
    parser_repo_events.add_argument('--page', help='Page number to display')
    parser_repo_events.set_defaults(func=repo_events)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

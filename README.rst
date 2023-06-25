=============
GitHub Events Analyzer
=============

This is a simple Python package that provides an easy interface to the GitHub API for fetching repository events. It includes a command line interface (CLI) for fetching and analyzing events from a specific GitHub repository.

Features
========

- Fetch events from any public GitHub repository.
- Count the different types of events in the repository.
- Identify the most active user in the repository based on the number of events.

Usage
=====

As a Module
-----------
The GitHub API interface can be used in your own Python scripts. Here is a basic usage example:

.. code-block:: python

    from github_events_analyser.github_api import GitHubAPI
    
    # Initialize the GitHubAPI object
    api = GitHubAPI('YOUR_GITHUB_TOKEN')
    
    # Fetch the events of a repository
    response = api.get_repo_events('USERNAME', 'REPO')
    
    # Process the response here...

Command Line Interface (CLI)
----------------------------

The CLI provides a way to fetch and analyze GitHub events directly from the command line. 

To fetch the events of a repository:

.. code-block:: shell

    python cli.py repo-events --token YOUR_GITHUB_TOKEN USERNAME REPO

Arguments:

- `USERNAME`: The GitHub username to fetch events for.
- `REPO`: The GitHub repository to fetch events for.
- `--per-page`: (Optional) Number of events to display per page (max 100).
- `--event-type`: (Optional) The type of event to fetch. e.g., "PushEvent", "PullRequestEvent".
- `--page`: (Optional) Page number to display.
- `--order`: (Optional) Chronological order of events. Enter 'a' for ascending or 'd' for descending order.

Running Tests
=============

To run the tests:

.. code-block:: shell

    python -m unittest

Ensure that you are in the top level directory (same level as the tests directory) when running this command.


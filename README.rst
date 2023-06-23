.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=================================
GitHub Events Analyser
=================================

GitHub Events Analyser is a Python-based command-line interface for fetching and analyzing events data from GitHub.

Features
========

With GitHub Events Analyser, you can:

* Retrieve information about a specific GitHub user.
* Get a list of events associated with a user.
* Filter events based on event types such as "PushEvent", "PullRequestEvent" and more.

Installation
============

To install GitHub Events Analyser, clone the repository, navigate into the project directory, and install the required dependencies:

.. code-block:: bash

    git clone https://github.com/ZakYeo/github-events-analyser.git
    cd github-events-analyser
    pip install -r requirements.txt

CLI Usage
=========

Here are examples of how to use the command-line interface:

.. code-block:: bash

    # To fetch user information:
    github-events-analyser --token your_github_token user-info github_username

    # To fetch and filter user events:
    github-events-analyser --token your_github_token user-events github_username --event-type PushEvent

Replace `your_github_token` with your personal access token from GitHub, and `github_username` with the username you want to fetch information for.

Module Usage
============

You can also use GitHub Events Analyser as a module in your Python projects. The `GitHubAPI` class provides methods for accessing user and repository event data from GitHub.

Here's a basic usage example:

.. code-block:: python

    from github_events_analyser.github_api import GitHubAPI

    # Initialize the API with your GitHub token
    api = GitHubAPI('your_github_token')

    # Fetch user information
    user_info = api.get_user_info('github_username')
    print(user_info)

    # Fetch user events
    user_events = api.get_user_events('github_username')
    print(user_events)

    # Fetch specific user events (for example, only PushEvents)
    push_events = api.get_user_events('github_username', 'PushEvent')
    print(push_events)

    # Fetch repository events
    repo_events = api.get_repo_events('github_username', 'repo_name')
    print(repo_events)

Replace `'your_github_token'`, `'github_username'`, and `'repo_name'` with your actual GitHub token, GitHub username, and repository name, respectively.

Running Unit Tests
==================

To run the unit tests for this project, follow these steps:

.. code-block:: bash

    # Clone the repository
    git clone https://github.com/ZakYeo/github-events-analyser.git

    # Navigate to the root directory of the project
    cd github-events-analyser

    # Install the package in editable mode along with its dependencies
    pip install -e .

    # Run the unit tests
    python -m unittest discover tests

If the tests run successfully, you'll see output indicating the number of tests run and that all tests passed. If any tests fail, you'll see output indicating which tests failed and a traceback to where in the code the failure occurred.

Notes
=====

This project has been set up using PyScaffold 4.5. For details and usage information on PyScaffold see https://pyscaffold.org/.

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

======================
github-events-analyser
======================

This is a Python-based command-line interface for fetching and analyzing events data from GitHub. 

It can fetch information about a specific user as well as filter events based on types. 

With the `github-events-analyser` you can:

- Retrieve information about a specific GitHub user
- Get a list of events associated with a user
- Filter events based on event types such as "PushEvent", "PullRequestEvent" and more

Installation
============

To install `github-events-analyser`, first clone the repository:

.. code-block:: bash

    git clone https://github.com/ZakYeo/github-events-analyser.git

Then, navigate into the project directory:

.. code-block:: bash

    cd github-events-analyser

And install the required dependencies:

.. code-block:: bash

    pip install -r requirements.txt

CLI Usage
=====

To fetch user information:

.. code-block:: bash

    github-events-analyser --token your_github_token user-info github_username

To fetch and filter user events:

.. code-block:: bash

    github-events-analyser --token your_github_token user-events github_username --event-type PushEvent

Replace `your_github_token` with your personal access token from GitHub and `github_username` with the username you want to fetch information for.

.. _pyscaffold-notes:

Module Usage
===============

You can also use the `github-events-analyser` as a module in your own Python projects. The `GitHubAPI` class provides easy-to-use methods for accessing user and repository event data from GitHub. 

Here is a basic usage example:

.. code-block:: python

    from github_events_analyser.github_api import GitHubAPI

    # Initialize the API with your GitHub token
    api = GitHubAPI('<your GitHub token>')

    # Fetch user information
    user_info = api.get_user_info('<username>')
    print(user_info)

    # Fetch user events
    user_events = api.get_user_events('<username>')
    print(user_events)

    # Fetch specific user events (for example, only PushEvents)
    push_events = api.get_user_events('<username>', 'PushEvent')
    print(push_events)

    # Fetch repository events
    repo_events = api.get_repo_events('<username>', '<repo name>')
    print(repo_events)

Remember to replace `'<your GitHub token>'`, `'<username>'`, and `'<repo name>'` with your actual GitHub token, GitHub username, and repository name, respectively. Also, ensure you have the required permissions for the GitHub token to access private repositories and user data.


Note
====

This project has been set up using PyScaffold 4.5. For details and usage information on PyScaffold see https://pyscaffold.org/.

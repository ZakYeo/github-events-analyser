.. image:: https://api.cirrus-ci.com/github/<USER>/github-events-analyser.svg?branch=main
    :alt: Built Status
    :target: https://cirrus-ci.com/github/<USER>/github-events-analyser
.. image:: https://readthedocs.org/projects/github-events-analyser/badge/?version=latest
    :alt: ReadTheDocs
    :target: https://github-events-analyser.readthedocs.io/en/stable/
.. image:: https://img.shields.io/coveralls/github/<USER>/github-events-analyser/main.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/<USER>/github-events-analyser
.. image:: https://img.shields.io/pypi/v/github-events-analyser.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/github-events-analyser/
.. image:: https://img.shields.io/conda/vn/conda-forge/github-events-analyser.svg
    :alt: Conda-Forge
    :target: https://anaconda.org/conda-forge/github-events-analyser
.. image:: https://pepy.tech/badge/github-events-analyser/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/github-events-analyser
.. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
    :alt: Twitter
    :target: https://twitter.com/github-events-analyser

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

===========
Installation
============

You can install `github-events-analyser` using pip:

```bash
pip install github-events-analyser
```

======================
Usage
======================
To fetch user information:

`github-events-analyser --token your_github_token user-info github_username`

To fetch and filter user events:

`github-events-analyser --token your_github_token user-events github_username --event-type PushEvent`

Replace your_github_token with your personal access token from GitHub and github_username with the username you want to fetch information for.


======================
Note
======================
This project has been set up using PyScaffold 4.5. For details and usage information on PyScaffold see https://pyscaffold.org/.
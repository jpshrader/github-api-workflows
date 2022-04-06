# Iniúchóir Github

This is the GitHub Auditor.

### Setup

1. Install [VS Code](https://code.visualstudio.com/download)
2. Install [Python Extensions](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for VS Code
3. Install pip
    * `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
    * `python3 get-pip.py`
4. Install project dependencies
    * `pip3 install -r requirements.txt`

### Common Issues
1. If you receive errors around [`PyGitHub`](https://github.com/PyGithub/PyGithub) (`ImportError: No module named github`), you may need to change VS Code's Python interpreter
    * Hit `⌘ P`
    * Type `>Python: Select Interpreter`
    * Select the `Global` option in the drop down list
        * If there is no `Global` option, try each option until VS Code can resolve the dependencies.
2. If for whatever reason you commit your Personal Access Token and push it, GitHub will automatically delete that token from your account.

Notes:
1. [PyGitHub API Reference](https://pygithub.readthedocs.io/en/latest/apis.html)
2. [PyGitHub API Object Reference](https://pygithub.readthedocs.io/en/latest/github_objects.html)
3. [Python Requirements file](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
4. [VS Code Python Interpreter Selector](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
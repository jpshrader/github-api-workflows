'''Interprets release commands from an instruction block'''

from github import Github

from github_functions.release_management import create_release as create_new_release
from github_interpreter.argument_interpreter import retrieve_argument

def create_release(github: Github, instruction) -> None:
    '''Creates a release branch'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    from_branch = retrieve_argument(instruction, 'from_branch')
    to_branch = retrieve_argument(instruction, 'to_branch')
    tag = retrieve_argument(instruction, 'tag')
    release = retrieve_argument(instruction, 'release', is_required=False, default=None)
    pull_request_options = retrieve_argument(instruction, 'pull_request_options', is_required=False, default=None)

    create_new_release(github, repo_name, from_branch, to_branch, tag, release, pull_request_options)

'''Label management service'''
from github import Github, GithubException

from github_services.label_service import get_label, create_label, update_label

def create_or_update_label(github: Github, label_name: str, label_color: str, label_description: str, repos: list[str]) -> None:
    '''Create or updates a given label in a given repo'''
    for repo in repos:
        if label_exists(github, repo, label_name):
            update_label(github, repo, label_name, label_color, label_description)
            print(f'UPDATED label {label_name} on {repo}')
        else:
            create_label(github, repo, label_name, label_color, label_description)
            print(f'CREATED label {label_name} on {repo}')

def label_exists(github: Github, repo_full_name: str, label_name: str) -> bool:
    '''Determines whether a given label exists in a given repo'''
    try:
        label = get_label(github, repo_full_name, label_name)
        return label is not None
    except GithubException as exp:
        if exp.status == 404:
            return False
        raise exp

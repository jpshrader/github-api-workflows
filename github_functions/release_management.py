'''Release management service'''

from github import Github

from github_services.repo_service import get_repo_by_full_name
from github_services.comparison_service import is_branch_ahead_with_repo
from github_services.branch_service import create_branch_from_repo, merge_branches_from_repo

def create_release(github: Github, repo_full_name: str, from_branch: str, to_branch: str, tag, release, pull_request_options) -> None:
    '''Performs a series of actions to bootstrap a new release'''
    new_from_branch = tag.branch_name
    repo = get_repo_by_full_name(github, repo_full_name)
    if is_branch_ahead_with_repo(repo, to_branch, from_branch):
        create_branch_from_repo(repo, to_branch, new_from_branch)
        merge_branches_from_repo(repo, new_from_branch, from_branch, f'Merge {from_branch} to {new_from_branch}')

'''Branch Management Service'''
from datetime import datetime
from github import Github, Branch, Repository, Label

from github_services.comparison_service import is_branch_ahead
from github_services.repo_service import get_repo_by_full_name
from github_services.pull_request_service import create_pull_request_by_repo
from github_services.branch_service import delete_branch_from_repo_by_branch, get_branch_from_list, create_branch_from_repo

def merge_branch_and_pr(github: Github, repo_full_name: str, from_branch: str, to_branch: str, reviewers: list[str], labels: list[str]) -> None:
    '''Opens a Pr to update a given branch'''
    date_time = datetime.now().strftime("%d-%m-%YT%H-%M-%S")
    new_branch_name = f'merge-{from_branch}-to-{to_branch}-{date_time}'
    repo = get_repo_by_full_name(github, repo_full_name)
    create_branch_from_repo(repo, from_branch, new_branch_name)

    pr_name = f'Merge {from_branch} to {to_branch}'
    pull_request = create_pull_request_by_repo(repo, pr_name, '', to_branch, new_branch_name, is_draft=False)

    for label in labels:
        pull_request.add_to_labels(label)
    pull_request.create_review_request(reviewers)

def identify_empty_branches(github: Github, repo_full_name: str, target_branch: str) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return identify_empty_branches_with_repo(repo, target_branch)

def identify_empty_branches_with_repo(repo: Repository.Repository, target_branch: str) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    empty_branches = []
    branches = repo.get_branches()
    target = get_branch_from_list(branches, target_branch)

    for branch in branches:
        if target.name != branch.name and not(branch.protected) and not is_branch_ahead(repo, target, branch):
            empty_branches.append(branch)

    return empty_branches

def delete_empty_branches(github: Github, repo_full_name: str, target_branch: str) -> None:
    '''Deletes branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    branches = identify_empty_branches_with_repo(repo, target_branch)

    for branch in branches:
        delete_branch_from_repo_by_branch(repo, branch)

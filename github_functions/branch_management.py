'''Branch Management Service'''
from datetime import date
from github import Github, Branch, Repository, PullRequest

from github_services.branch_service import delete_branch_from_repo_by_branch, get_branch_from_list, create_branch
from github_services.comparison_service import is_branch_ahead
from github_services.repo_service import get_repo_by_full_name
from github_services.pull_request_service import create_pull_request

def update_branch(github: Github, repo_full_name: str, from_branch: str, to_branch: str) -> PullRequest.PullRequest:
    '''Opens a Pr to update a given branch'''
    new_branch_name = f'merge-{from_branch}-to-{to_branch}-{date.today()}'
    new_ref = create_branch(github, repo_full_name, from_branch, new_branch_name)

    pr_name = 'Merge {from_branch} to {to_branch}'
    return create_pull_request(github, repo_full_name, pr_name, '', f'refs/heads/{to_branch}', new_ref.ref, is_draft=True)


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

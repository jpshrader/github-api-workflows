'''Branch Management Service'''
from github import Github, Branch, Repository

from src.github_services.branch_service import delete_branch_from_repo_by_branch, get_branch_from_list
from src.github_services.comparison_service import is_branch_ahead
from src.github_services.repo_service import get_repo_by_full_name

def identify_empty_branches(github: Github, repo_full_name: str, taget_branch: str) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return identify_empty_branches_with_repo(repo, taget_branch)

def identify_empty_branches_with_repo(repo: Repository.Repository, taget_branch: str) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    empty_branches = []
    branches = repo.get_branches()
    target = get_branch_from_list(branches, taget_branch)

    for branch in branches:
        if target.name != branch.name and not(branch.protected) and not is_branch_ahead(repo, target, branch):
            empty_branches.append(branch)

    return empty_branches

def delete_empty_branches(github: Github, repo_full_name: str, taget_branch: str):
    '''Deletes branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    branches = identify_empty_branches_with_repo(repo, taget_branch)

    for branch in branches:
        delete_branch_from_repo_by_branch(repo, branch)

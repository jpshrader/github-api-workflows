'''GitHub Branch Comparison Service'''
from github import Branch, Repository, Comparison, Github

from github_services.branch_service import get_branch_from_repo
from github_services.repo_service import get_repo_by_full_name

# GET COMPARISON
def compare_branches(github: Github, repo_full_name: str, to_branch: str, from_branch: str) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return compare_branches_with_repo(repo, to_branch, from_branch)

def compare_branches_with_repo(repo: Repository.Repository, to_branch: str, from_branch: str) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    target_branch = get_branch_from_repo(repo, to_branch)
    origin_branch = get_branch_from_repo(repo, from_branch)
    return compare_branches_with_repo_and_branches(repo, target_branch, origin_branch)

def compare_branches_with_repo_and_branches(repo: Repository.Repository, to_branch: Branch.Branch, from_branch: Branch.Branch) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    return repo.compare(to_branch.commit.commit.sha, from_branch.commit.commit.sha)

# COMPARE BRANCHES
def is_branch_ahead(github: Github, repo_full_name: str, to_branch: str, from_branch: str) -> bool:
    '''Determines whether from_branch is 1 or more commits ahead of to_branch'''
    comparison = compare_branches(github, repo_full_name, to_branch, from_branch)
    return is_ahead(comparison)

def is_branch_ahead_with_repo(repo: Repository.Repository, to_branch: str, from_branch: str) -> bool:
    '''Determines whether from_branch is 1 or more commits ahead of to_branch'''
    comparison = compare_branches_with_repo(repo, to_branch, from_branch)
    return is_ahead(comparison)

# COMPARISON UTILS
def is_ahead(comparison: Comparison.Comparison) -> bool:
    '''Branch is 1 or more commits ahead of target'''
    return comparison.ahead_by > 0

def is_ahead_with_branch(repo: Repository.Repository, to_branch: Branch.Branch, from_branch: Branch.Branch) -> bool:
    '''Branch is 1 or more commits ahead of target'''
    comparison = compare_branches_with_repo_and_branches(repo, to_branch, from_branch)
    return is_ahead(comparison)

def is_behind(comparison: Comparison.Comparison) -> bool:
    '''Branch is 1 or more commits behind target'''
    return comparison.behind_by > 0

def is_behind_with_branch(repo: Repository.Repository, to_branch: Branch.Branch, from_branch: Branch.Branch) -> bool:
    '''Branch is 1 or more commits behind target'''
    comparison = compare_branches_with_repo_and_branches(repo, to_branch, from_branch)
    return is_behind(comparison)

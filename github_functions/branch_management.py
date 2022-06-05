'''Branch Management Service'''
from datetime import datetime
from github import Github, Branch, Repository

from github_services.user_service import get_current_user
from github_services.comparison_service import is_branch_ahead
from github_services.repo_service import get_repo_by_full_name
from github_services.pull_request_service import create_pull_request_by_repo
from github_services.branch_service import delete_branch_from_repo_by_branch, get_branch_from_list, create_branch_from_repo

def branch_passes_filters(branch: Branch.Branch, include: list[str], exclude: list[str]):
    '''Determines whether a branch name is filtered by include/exclude rules'''
    include_passes = len(include) == 0
    exclude_passes = len(exclude) == 0

    for inc in include:
        inc = inc.strip()
        if inc == '' or inc.lower() in branch.name.lower():
            include_passes = True

    for ex in exclude:
        ex = ex.strip()
        if ex == '' or ex.lower() not in branch.name.lower():
            exclude_passes = True

    return include_passes and exclude_passes

# MERGE AND PR BRANCH
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

    if len(reviewers) > 0:
        reviewers_to_request = []
        current_user = get_current_user(github)
        for reviewer in reviewers:
            if reviewer != current_user.login:
                reviewers_to_request.append(reviewer)
        pull_request.create_review_request(reviewers_to_request)

# IDENTIFY UNPROTECTED BRANCHES
def identify_unprotected_branches(github: Github, repo_full_name: str, include: list[str] = None, exclude: list[str] = None) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return identify_unprotected_branches_with_repo(repo, include=include, exclude=exclude)

def identify_unprotected_branches_with_repo(repo: Repository.Repository, include: list[str] = None, exclude: list[str] = None) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    unprotected_branches = []
    branches = repo.get_branches()
    for branch in branches:
        if not branch.protected and branch_passes_filters(branch, include, exclude):
            unprotected_branches.append(branch)

    return unprotected_branches

# IDENTIFY EMPTY BRANCHES
def identify_empty_branches(github: Github, repo_full_name: str, target_branch: str = '', include: list[str] = None, exclude: list[str] = None) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return identify_empty_branches_with_repo(repo, target_branch, include=include, exclude=exclude)

def identify_empty_branches_with_repo(repo: Repository.Repository, target_branch: str = '', include: list[str] = None, exclude: list[str] = None) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    if target_branch == '':
        target_branch = repo.default_branch

    empty_branches = []
    branches = repo.get_branches()
    target = get_branch_from_list(branches, target_branch)

    for branch in branches:
        if target.name != branch.name and not(branch.protected) and not is_branch_ahead(repo, target, branch) and branch_passes_filters(branch, include, exclude):
            empty_branches.append(branch)

    return empty_branches

def delete_empty_branches(github: Github, repo_full_name: str, target_branch: str) -> None:
    '''Deletes branches that are empty (not ahead of target branch)'''
    repo = get_repo_by_full_name(github, repo_full_name)
    branches = identify_empty_branches_with_repo(repo, target_branch)

    for branch in branches:
        delete_branch_from_repo_by_branch(repo, branch)

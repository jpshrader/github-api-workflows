'''Interprets branch commands from an instruction block'''
from github import Github, Branch

from github_interpreter.argument_interpreter import retrieve_argument
from github_functions.branch_management import merge_branch_and_pr, identify_empty_branches, identify_unprotected_branches, delete_empty_branches as remove_empty_branches

def print_branch_list(branch_list: list[Branch.Branch], action: str, repo_name: str, include: list[str], exclude: list[str]):
    '''Prints a list of branches associated with a particular action'''
    print('=' * 30)
    print(f'{len(branch_list)} {action} BRANCHES FOUND IN {repo_name}')
    if len(include) > 0:
        include_list = ', '.join(include)
        print(f'Include branches containing: {include_list}')
    if len(exclude) > 0:
        exclude_list = ', '.join(exclude)
        print(f'Exclude branches containing: {exclude_list}')
    for empty_branch in branch_list:
        print(f'  - {empty_branch.name}')

def merge_branch(github: Github, instruction) -> None:
    '''Opens a PR to update a branch'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    from_branch = retrieve_argument(instruction, 'from_branch')
    to_branch = retrieve_argument(instruction, 'to_branch')
    reviewers = retrieve_argument(instruction, 'reviewers', is_required=False, default=[])
    labels = retrieve_argument(instruction, 'labels', is_required=False, default=[])
    title = retrieve_argument(instruction, 'title', is_required=False, default=f'Merge {from_branch} to {to_branch}')

    merge_branch_and_pr(github, repo_name, from_branch, to_branch, reviewers, labels, title)

def list_empty_branches(github: Github, instruction) -> None:
    '''Lists all empty branches in a given repo'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    target_branch = retrieve_argument(instruction, 'target_branch', is_required=False, default='')
    include = retrieve_argument(instruction, 'include', is_required=False, default=[])
    exclude = retrieve_argument(instruction, 'exclude', is_required=False, default=[])

    empty_branches = identify_empty_branches(github, repo_name, target_branch=target_branch, include=include, exclude=exclude)
    print_branch_list(empty_branches, 'EMPTY', repo_name, include, exclude)

def delete_empty_branches(github: Github, instruction) -> None:
    '''Deletes all empty branches in a given repo'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    target_branch = retrieve_argument(instruction, 'target_branch', is_required=False, default='')
    include = retrieve_argument(instruction, 'include', is_required=False, default=[])
    exclude = retrieve_argument(instruction, 'exclude', is_required=False, default=[])

    remove_empty_branches(github, repo_name, target_branch=target_branch, include=include, exclude=exclude)

def list_unprotected_branches(github: Github, instruction) -> None:
    '''Lists all branches that are not protected'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    include = retrieve_argument(instruction, 'include', is_required=False, default=[])
    exclude = retrieve_argument(instruction, 'exclude', is_required=False, default=[])

    empty_branches = identify_unprotected_branches(github, repo_name, include=include, exclude=exclude)
    print_branch_list(empty_branches, 'UNPROTECTED', repo_name, include, exclude)

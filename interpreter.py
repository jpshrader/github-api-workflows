'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError
from typing import Dict

from github import Github, Branch
from github_functions.branch_management import identify_empty_branches, merge_branch_and_pr, identify_unprotected_branches

def retrieve_argument(instruction, argument: str, is_required: bool = True, default = None):
    '''Retrives an instruction argument - defaults to `default` if not required'''
    if not is_required:
        value = default
        if argument in instruction:
            value = instruction[argument]
        return value

    return instruction[argument]

def print_branch_list(branch_list: list[Branch.Branch], action: str, repo_name: str, include: str, exclude: str):
    '''Prints a list of branches associated with a particular action'''
    print('=' * 30)
    print(f'{len(branch_list)} {action} BRANCHES FOUND IN {repo_name}')
    if include != '':
        print(f'Include branches containing: {include.lower()}')
    if exclude != '':
        print(f'Exclude branches containing: {exclude.lower()}')
    for empty_branch in branch_list:
        print(f'  - {empty_branch.name}')

def merge_branch(github: Github, instruction) -> None:
    '''Opens a PR to update a branch'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    from_branch = retrieve_argument(instruction, 'from_branch')
    to_branch = retrieve_argument(instruction, 'to_branch')
    reviewers = retrieve_argument(instruction, 'reviewers', is_required=False, default='')
    labels = retrieve_argument(instruction, 'labels', is_required=False, default='')

    merge_branch_and_pr(github, repo_name, from_branch, to_branch, reviewers, labels)

def list_empty_branches(github: Github, instruction) -> None:
    '''Lists all empty branches in a given repo'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    include = retrieve_argument(instruction, 'include', is_required=False, default=[])
    exclude = retrieve_argument(instruction, 'exclude', is_required=False, default=[])

    empty_branches = identify_empty_branches(github, repo_name, include=include, exclude=exclude)
    print_branch_list(empty_branches, 'EMPTY', repo_name, include, exclude)

def list_unprotected_branches(github: Github, instruction) -> None:
    '''Lists all branches that are not protected'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    include = retrieve_argument(instruction, 'include', is_required=False, default=[])
    exclude = retrieve_argument(instruction, 'exclude', is_required=False, default=[])

    empty_branches = identify_unprotected_branches(github, repo_name, include=include, exclude=exclude)
    print_branch_list(empty_branches, 'UNPROTECTED', repo_name, include, exclude)

def interpret_instructions(github: Github, instructions: Dict[str, object]) -> None:
    '''Interprets and executes a sequence of instructions'''
    for instruction in instructions['instructions']:
        match str(instruction['action']).lower():
            case 'merge_branch':
                merge_branch(github, instruction)
            case 'list_empty_branches':
                list_empty_branches(github, instruction)
            case 'list_unprotected_branches':
                list_unprotected_branches(github, instruction)

            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

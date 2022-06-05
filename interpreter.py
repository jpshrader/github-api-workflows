'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError
from typing import Dict

from github import Github
from github_functions.branch_management import identify_empty_branches, merge_branch_and_pr

def retrieve_argument(instruction, argument: str, is_required: bool = True):
    '''Retrives an instruction argument - defaults to empty string if not required'''
    if not is_required:
        value = ''
        if argument in instruction:
            value = instruction[argument]
        return value

    return instruction[argument]

def merge_branch(github: Github, instruction) -> None:
    '''Opens a PR to update a branch'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    from_branch = retrieve_argument(instruction, 'from_branch')
    to_branch = retrieve_argument(instruction, 'to_branch')
    reviewers = retrieve_argument(instruction, 'reviewers', is_required=False)
    labels = retrieve_argument(instruction, 'labels', is_required=False)

    merge_branch_and_pr(github, repo_name, from_branch, to_branch, reviewers, labels)

def list_empty_branches(github: Github, instruction) -> None:
    '''Lists all empty branches in a given repo'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    include_filter = retrieve_argument(instruction, 'include_filter', is_required=False)
    exclude_filter = retrieve_argument(instruction, 'exclude_filter', is_required=False)

    empty_branches = identify_empty_branches(github, repo_name, include_filter=include_filter, exclude_filter=exclude_filter)
    print('=' * 30)
    print(f'{len(empty_branches)} EMPTY BRANCHES FOUND IN {repo_name}')
    for empty_branch in empty_branches:
        print(f'  - {empty_branch.name}')

def interpret_instructions(github: Github, instructions: Dict[str, object]) -> None:
    '''Interprets and executes a sequence of instructions'''
    for instruction in instructions['instructions']:
        match instruction['action']:
            case 'merge_branch':
                merge_branch(github, instruction)
            case 'list_empty_branches':
                list_empty_branches(github, instruction)

            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

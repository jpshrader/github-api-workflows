'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError
from typing import Dict

from github import Github
from github_functions.branch_management import identify_empty_branches, merge_branch_and_pr

def merge_branch(github: Github, instruction) -> None:
    '''Opens a PR to update a branch'''
    repo_name = instruction['repo_name']
    from_branch = instruction['from_branch']
    to_branch = instruction['to_branch']
    reviewers = instruction['reviewers']
    labels = instruction['labels']

    merge_branch_and_pr(github, repo_name, from_branch, to_branch, reviewers, labels)

def list_empty_branches(github: Github, instruction) -> None:
    '''Lists all empty branches in a given repo'''
    repo_name = instruction['repo_name']
    filter_field_name = 'branch_filter'
    branch_name_filter = ''
    if filter_field_name in instruction:
        branch_name_filter = instruction['branch_filter']

    empty_branches = identify_empty_branches(github, repo_name, branch_name_filter=branch_name_filter)
    print('=' * 30)
    print(f'{len(empty_branches)} EMPTY BRANCHES FOUND IN {repo_name}')
    for empty_branch in empty_branches:
        print(f'  - {empty_branch.name}')

def interpret_instructions(github: Github, instructions: Dict[str, object]) -> None:
    '''Interprets and executes a sequence of instructions'''
    instruction_list = instructions['instructions']

    for i in range(len(instruction_list)): # pylint: disable=consider-using-enumerate
        instruction = instruction_list[i]
        match instruction['action']:
            case 'merge_branch':
                merge_branch(github, instruction)
                break
            case 'list_empty_branches':
                list_empty_branches(github, instruction)
                break

            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

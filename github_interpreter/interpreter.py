'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError
from typing import Dict

from github import Github
from github_interpreter.argument_interpreter import retrieve_argument
from github_interpreter.branch_interpreter import merge_branch, list_empty_branches, delete_empty_branches, list_unprotected_branches

def create_release(github: Github, instruction) -> None:
    '''Creates a release branch'''
    repo_name = retrieve_argument(instruction, 'repo_name')
    from_branch = retrieve_argument(instruction, 'from_branch')
    to_branch = retrieve_argument(instruction, 'to_branch')
    tag = retrieve_argument(instruction, 'tag')
    tag = retrieve_argument(instruction, 'tag')
    reviewers = retrieve_argument(instruction, 'reviewers', is_required=False, default='')
    labels = retrieve_argument(instruction, 'labels', is_required=False, default='')

def interpret_instructions(github: Github, instructions: Dict[str, object]) -> None:
    '''Interprets and executes a sequence of instructions'''
    for instruction in instructions['instructions']:
        match str(instruction['action']).lower():
            case 'merge_branch':
                merge_branch(github, instruction)
            case 'list_empty_branches':
                list_empty_branches(github, instruction)
            case 'delete_empty_branches':
                delete_empty_branches(github, instruction)
            case 'list_unprotected_branches':
                list_unprotected_branches(github, instruction)
            case 'create_release':
                create_release(github, instruction)

            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

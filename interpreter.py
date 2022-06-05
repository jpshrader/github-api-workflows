'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError
from typing import Dict

from github import Github
from github_functions.branch_management import update_branch

def merge_branch(github: Github, instruction) -> None:
    '''Opens a PR to update a branch'''
    repo_name = instruction['repo_name']
    from_branch = instruction['from_branch']
    to_branch = instruction['to_branch']
    update_branch(github, repo_name, from_branch, to_branch)

def interpret_instructions(github: Github, instructions: Dict[str, object]) -> None:
    '''Interprets and executes a sequence of instructions'''
    for instruction in instructions['instructions']:
        match instruction['action']:
            case 'merge_branch':
                merge_branch(github, instruction)
                break

            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

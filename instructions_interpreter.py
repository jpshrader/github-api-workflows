'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError

from github import Github
from instructions import Instructions
from github_functions.branch_management import update_branch

def interpret_instructions(github: Github, instructions: Instructions) -> None:
    '''Interprets and executes a sequence of instructions'''

    for instruction in instructions.instructions:
        match instruction.action:
            case 'merge_branch':
                repo_name = instruction.repo_name
                from_branch = instruction.from_branch
                to_branch = instruction.to_branch
                return update_branch(github, repo_name, from_branch, to_branch)

            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

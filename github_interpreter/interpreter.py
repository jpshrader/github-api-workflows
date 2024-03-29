'''Interpreter engine for GitHub Utility'''
from argparse import ArgumentError
from typing import Dict

from github import Github
from github_interpreter.branch_interpreter import merge_branch, list_empty_branches, delete_empty_branches, list_unprotected_branches
from github_interpreter.label_intepreter import create_label

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
            case 'create_label':
                create_label(github, instruction)
            case _:
                raise ArgumentError(None, f'{instruction.action} is not a supported action')

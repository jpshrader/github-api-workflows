'''Interprets branch commands from an instruction block'''
from github import Github

from github_interpreter.argument_interpreter import retrieve_argument
from github_functions.label_management import create_or_update_label

def create_label(github: Github, instruction) -> None:
    '''Create or updates a given label in a given repo'''
    repos = retrieve_argument(instruction, 'repos')
    name = retrieve_argument(instruction, 'name')
    color = retrieve_argument(instruction, 'color')
    description = retrieve_argument(instruction, 'description', is_required=False, default='')

    create_or_update_label(github, name, color, description, repos)

'''Argument parsing utilities'''
import argparse

from file_helper import get_file, YAML_FILE_TYPE

BASE_PATH_ARG = 'base_path'
FILE_TYPE_ARG = 'file_type'
ACCESS_TOKEN_ARG = 'access_token'
INSTRUCTIONS_FILE_ARG = 'instructions'

class CommandLineArgs: # pylint: disable=too-few-public-methods
    '''Command line argument object'''
    data_type: str
    base_path: str
    access_token: str
    instructions: object

    def __init__(self, instructions: object, data_type: str, base_path: str, access_token: str):
        self.data_type = data_type
        self.base_path = base_path
        self.access_token = access_token
        self.instructions = instructions

def parse_args() -> CommandLineArgs:
    '''Retrieves command line arguments to this python application'''
    parser = argparse.ArgumentParser()

    parser.add_argument(f'--{BASE_PATH_ARG}', default='', type=str)
    file_type_action = parser.add_argument(f'--{FILE_TYPE_ARG}', default='', type=str)
    access_token_action = parser.add_argument(f'--{ACCESS_TOKEN_ARG}', default='', type=str)
    instructions_file_action = parser.add_argument(f'--{INSTRUCTIONS_FILE_ARG}', default='', type=str)

    args = vars(parser.parse_args())

    file_type = args[FILE_TYPE_ARG]
    if file_type == '':
        raise_required_arg_error(file_type_action, FILE_TYPE_ARG)

    if file_type not in (YAML_FILE_TYPE):
        raise argparse.ArgumentError(file_type_action, message=f'{FILE_TYPE_ARG} must be in: (`{YAML_FILE_TYPE}`)')

    instruction_arg = args[INSTRUCTIONS_FILE_ARG]
    if instruction_arg == '':
        raise_required_arg_error(instructions_file_action, INSTRUCTIONS_FILE_ARG)

    instructions = None
    if instruction_arg != '':
        instructions = get_file(instruction_arg, file_type)

    access_token = args[ACCESS_TOKEN_ARG]
    if access_token == '':
        raise_required_arg_error(access_token_action, ACCESS_TOKEN_ARG)

    return CommandLineArgs(instructions, file_type, args[BASE_PATH_ARG], access_token)

def raise_required_arg_error(action, arg_name):
    '''Returns a new ArgumentError for a given argument'''
    raise argparse.ArgumentError(action, message=f'`{arg_name}` is a required argument')

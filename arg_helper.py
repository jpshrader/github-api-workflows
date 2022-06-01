'''Argument parsing utilities'''
import argparse

from file_helper import get_file, get_data, YAML_FILE_TYPE

BASE_PATH_ARG = 'base_path'
FILE_TYPE_ARG = 'file_type'
INSTRUCTIONS_ARG = 'instructions'
ACCESS_TOKEN_ARG = 'access_token'

class CommandLineArgs: # pylint: disable=too-few-public-methods
    '''Command line argument object'''
    data: object
    data_type: str
    base_path: str
    access_token: str

    def __init__(self, data: object, data_type: str, base_path: str, access_token: str):
        self.data = data
        self.data_type = data_type
        self.base_path = base_path
        self.access_token = access_token

def parse_args() -> CommandLineArgs:
    '''Retrieves command line arguments to this python application'''
    parser = argparse.ArgumentParser()

    parser.add_argument(f'--{BASE_PATH_ARG}', default='', type=str)
    file_type_action = parser.add_argument(f'--{FILE_TYPE_ARG}', default='', type=str)
    instruction_action = parser.add_argument(f'--{INSTRUCTIONS_ARG}', default='', type=str)
    access_token_action = parser.add_argument(f'--{ACCESS_TOKEN_ARG}', default='', type=str)

    args = vars(parser.parse_args())

    file_type = args[FILE_TYPE_ARG]
    if file_type == '':
        raise_required_arg_error(file_type_action, FILE_TYPE_ARG)

    if file_type not in (YAML_FILE_TYPE):
        raise argparse.ArgumentError(file_type_action, message=f'{FILE_TYPE_ARG} must be in: (`{YAML_FILE_TYPE}`)')

    instruction_arg = args[INSTRUCTIONS_ARG]
    if instruction_arg == '':
        raise_required_arg_error(instruction_action, INSTRUCTIONS_ARG)

    data = None
    if instruction_arg != '':
        data = get_data(instruction_arg, file_type)
    else:
        data = get_file(instruction_arg, file_type)

    access_token = args[ACCESS_TOKEN_ARG]
    if access_token == '':
        raise_required_arg_error(access_token_action, ACCESS_TOKEN_ARG)

    return CommandLineArgs(data, file_type, args[BASE_PATH_ARG], access_token)

def raise_required_arg_error(action, arg_name):
    '''Returns a new ArgumentError for a given argument'''
    raise argparse.ArgumentError(action, message=f'`{arg_name}` is a required argument')

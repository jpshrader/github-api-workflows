'''Argument parsing utilities'''
import argparse

from file_helper import get_file, get_data, JSON_FILE_TYPE, YAML_FILE_TYPE

FILE_DATA_ARG = 'file_data'
FILE_PATH_ARG = 'file_path'
FILE_TYPE_ARG = 'file_type'

class CommandLineArgs:
    '''Command line argument object'''
    data: str
    data_type: str

    def __init__(self, data: str, data_type: str):
        self.data = data
        self.data_type = data_type

def parse_args() -> CommandLineArgs:
    '''Retrieves command line arguments to this python application'''
    parser = argparse.ArgumentParser()

    parser.add_argument(f'--{FILE_PATH_ARG}', default='', type=str)
    file_data_action = parser.add_argument(f'--{FILE_DATA_ARG}', default='', type=str)
    file_type_action = parser.add_argument(f'--{FILE_TYPE_ARG}', default='', type=str)

    args = vars(parser.parse_args())

    file_type = args[FILE_TYPE_ARG]
    if file_type == '':
        raise argparse.ArgumentError(file_type_action, message=f'{FILE_TYPE_ARG} is a required argument')

    if file_type not in (JSON_FILE_TYPE, YAML_FILE_TYPE):
        raise argparse.ArgumentError(file_type_action, message=f'{FILE_TYPE_ARG} must be in: (`{JSON_FILE_TYPE}`, `{YAML_FILE_TYPE}`)')

    data_arg = args[FILE_DATA_ARG]
    file_arg = args[FILE_PATH_ARG]
    if data_arg == '' and file_arg == '':
        raise argparse.ArgumentError(file_data_action, message=f'One of `{FILE_DATA_ARG}` or `{FILE_PATH_ARG}` is required')

    data = ''
    if data_arg != '':
        data = get_data(data_arg, file_type)
    else:
        data = get_file(data_arg, file_type)

    return CommandLineArgs(data, file_type)

'''Application entry point'''
import common.settings_constants as constants

from common.arg_helper import parse_args
from common.interpreter import interpret_instructions
from common.file_helper import get_file, JSON_FILE_TYPE

from github_services.github_service_factory import get_github_service

if __name__ == '__main__':
    args = parse_args()

    settings = get_file(args.base_path + constants.SETTINGS_FILE, JSON_FILE_TYPE)
    github = get_github_service(args.access_token, settings[constants.ITEMS_PER_PAGE])

    interpret_instructions(github, args.instructions)

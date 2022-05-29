'''Application entry point'''
import settings_constants as constants

from file_helper import JSON_FILE_TYPE, get_file

from github_services.github_service_factory import get_github_service
from github_services.branch_service import get_branches_by_repo
from github_services.repo_service import get_user_repos

if __name__ == '__main__':
    FILE_TYPE = JSON_FILE_TYPE

    settings = get_file(constants.SETTINGS_FILE, FILE_TYPE)
    github = get_github_service(settings[constants.ACCESS_TOKEN], settings[constants.ITEMS_PER_PAGE])

    repos = get_user_repos(github)
    for repo in repos:
        print(f'Repo: {repo.full_name}')
        print('\tBranches:')
        branches = get_branches_by_repo(repo)
        for branch in branches:
            print(f'\t\t{branch.name}')

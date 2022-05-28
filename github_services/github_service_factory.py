'''GitHub Service Factory'''
from github import Github

def get_github_service(access_token: str, items_per_page: int) -> Github:
    '''Returns a GitHub service object'''
    github = Github(access_token)
    github.per_page = items_per_page

    return github

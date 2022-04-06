from github import Github

def getGitHubAccess(accessToken: str, itemsPerPage: int) -> Github:
    gh = Github(accessToken)
    gh.per_page = itemsPerPage

    return gh
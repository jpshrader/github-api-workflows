from github import Github

def getGithubService(accessToken: str, itemsPerPage: int) -> Github:
    gh = Github(accessToken)
    gh.per_page = itemsPerPage

    return gh
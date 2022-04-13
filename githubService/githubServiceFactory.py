from github import Github

def getGithubService(accessToken: str, itemsPerPage: int) -> Github:
    githubService = Github(accessToken)
    githubService.per_page = itemsPerPage

    return githubService
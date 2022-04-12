from github import Github

def getGitHubAccess(accessToken: str, itemsPerPage: int) -> Github:
    githubAccess = Github(accessToken)
    githubAccess.per_page = itemsPerPage

    return githubAccess
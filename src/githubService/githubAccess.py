from github import Github

def getGitHubAccess(accessToken) -> Github:
    return Github(accessToken)
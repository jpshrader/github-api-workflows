from github import Github

def getGitHubAccess(accessToken):
    return Github(accessToken)
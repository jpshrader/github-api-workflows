from github import Branch, Github

def getBranches(githubAccess: Github, repoName: str) -> list[Branch.Branch]:
    '''Returns all branches of a given repo.'''
    return githubAccess.get_repo(repoName).get_branches()

def getBranch(githubAccess: Github, repoName: str, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo.'''
    return githubAccess.get_repo(repoName).get_branch(branchName)
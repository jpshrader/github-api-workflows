from github import Branch, Repository, Github

def getBranches(githubAccess: Github, repoName: str) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    return githubAccess.get_repo(repoName).get_branches()

def getBranches(repo: Repository.Repository) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    return repo.get_branches()

def getBranch(githubAccess: Github, repoName: str, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    return githubAccess.get_repo(repoName).get_branch(branchName)

def getBranch(repo: Repository.Repository, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    return repo.get_branch(branchName)

def deleteBranch(githubAccess: Github, repoName: str, branchName: str):
    '''Deletes a given branch of a given repo'''
    ref = githubAccess.get_repo(repoName).get_git_ref(f"heads/{branchName}")
    ref.delete()

def deleteBranch(repo: Repository.Repository, branchName: str):
    '''Deletes a given branch of a given repo'''
    ref = repo.get_git_ref(f"heads/{branchName}")
    ref.delete()
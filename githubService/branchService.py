from github import Branch, Repository, Github

# GET BRANCHES
def getBranches(gh: Github, repoFullName: str) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    return gh.get_repo(repoFullName).get_branches()

def getBranches(repo: Repository.Repository) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    return repo.get_branches()

# GET BRANCH
def getBranch(gh: Github, repoFullName: str, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    return gh.get_repo(repoFullName).get_branch(branchName)

def getBranch(repo: Repository.Repository, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    return repo.get_branch(branchName)

# DELETE BRANCH
def deleteBranch(gh: Github, repoFullName: str, branchName: str):
    '''Deletes a given branch of a given repo'''
    ref = gh.get_repo(repoFullName).get_git_ref(f"heads/{branchName}")
    ref.delete()

def deleteBranch(repo: Repository.Repository, branchName: str):
    '''Deletes a given branch of a given repo'''
    ref = repo.get_git_ref(f"heads/{branchName}")
    ref.delete()
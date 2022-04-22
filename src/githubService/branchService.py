from github import Branch, Repository, Github

from githubService.repoService import getRepoByFullName

# GET BRANCHES
def getBranches(gh: Github, repoFullName: str) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return getBranchesByRepo(repo)

def getBranchesByRepo(repo: Repository.Repository) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    return repo.get_branches()

# GET BRANCH
def getBranch(gh: Github, repoFullName: str, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return getBranchFromRepo(repo, branchName)

def getBranchFromRepo(repo: Repository.Repository, branchName: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    return repo.get_branch(branchName)

def getBranchFromList(branches: list[Branch.Branch], branchName: str) -> Branch.Branch | None:
    '''Returns a given branch in a list of branches'''
    for branch in branches:
        if (branch.name == branchName):
            return branch
    return None

# DELETE BRANCH
def deleteBranch(gh: Github, repoFullName: str, branchName: str):
    '''Deletes a given branch of a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    ref = repo.get_git_ref(repo, f"heads/{branchName}")
    ref.delete()

def deleteBranchFromRepo(repo: Repository.Repository, branchName: str):
    '''Deletes a given branch of a given repo'''
    ref = repo.get_git_ref(f"heads/{branchName}")
    ref.delete()

def deleteBranchFromRepoByBranch(repo: Repository.Repository, branch: Branch.Branch):
    '''Deletes a given branch of a given repo'''
    ref = repo.get_git_ref(f"heads/{branch.name}")
    ref.delete()
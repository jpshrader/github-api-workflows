from github import Branch, Repository, Github

from githubService.branchService import getBranchFromList, deleteBranchFromRepo
from githubService.comparisonService import isBranchAhead
from githubService.repoService import getRepoByFullName

def identifyEmptyBranchesByName(gh: Github, repoFullName: str, targetBranch: str) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    repo = gh.get_repo(repoFullName)
    return identifyEmptyBranches(repo, targetBranch)

def identifyEmptyBranches(repo: Repository.Repository, targetBranch: str) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    emptyBranches = []
    branches = repo.get_branches()
    target = getBranchFromList(branches, targetBranch)

    for b in branches:
        if (target.name != b.name and not(b.protected) and not(isBranchAhead(repo, target, b))):
                emptyBranches.append(b)

    return emptyBranches

def deleteEmptyBranches(gh: Github, repoFullName: str, targetBranch: str):
    '''Deletes branches that are empty (not ahead of target branch)'''
    repo = getRepoByFullName(gh, repoFullName)
    branches = identifyEmptyBranches(repo, targetBranch)

    for branch in branches:
        deleteBranchFromRepo(repo, branch)
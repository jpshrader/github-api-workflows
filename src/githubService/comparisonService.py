from github import Branch, Repository, Comparison, Github

from githubService.branchService import getBranchFromRepo
from githubService.repoService import getRepoByFullName

# GET COMPARISON
def compareBranches(gh: Github, repoFullName: str, toBranch: str, fromBranch: str) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return compareBranchesWithRepo(repo, toBranch, fromBranch)

def compareBranchesWithRepo(repo: Repository.Repository, toBranch: str, fromBranch: str) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    targetBranch = getBranchFromRepo(repo, toBranch)
    originBranch = getBranchFromRepo(repo, fromBranch)
    return compareBranchesWithRepoAndBranches(repo, targetBranch, originBranch)

def compareBranchesWithRepoAndBranches(repo: Repository.Repository, toBranch: Branch.Branch, fromBranch: Branch.Branch) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    return repo.compare(toBranch.commit.commit.sha, fromBranch.commit.commit.sha)

# COMPARISON UTILS
def isAhead(comparison: Comparison.Comparison) -> bool:
    '''Branch is 1 or more commits ahead of target'''
    return comparison.ahead_by > 0

def isBranchAhead(repo: Repository.Repository, toBranch: Branch.Branch, fromBranch: Branch.Branch) -> bool:
    '''Branch is 1 or more commits ahead of target'''
    comparison = compareBranches(repo, toBranch, fromBranch)
    return isAhead(comparison)

def isBehind(comparison: Comparison.Comparison) -> bool:
    '''Branch is 1 or more commits behind target'''
    return comparison.behind_by > 0

def isBranchBehind(repo: Repository.Repository, toBranch: Branch.Branch, fromBranch: Branch.Branch) -> bool:
    '''Branch is 1 or more commits behind target'''
    comparison = compareBranches(repo, toBranch, fromBranch)
    return isBehind(comparison)
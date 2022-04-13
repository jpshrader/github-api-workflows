from github import Branch, Repository, Comparison, Github

# GET COMPARISON
def compareBranches(gh: Github, repoFullName: str, toBranch: str, fromBranch: str) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    repo = gh.get_repo(repoFullName)
    targetBranch = repo.get_branch(toBranch)
    originBranch = repo.get_branch(fromBranch)
    return repo.compare(targetBranch.commit.commit.sha, originBranch.commit.commit.sha)

def compareBranches(repo: Repository.Repository, toBranch: str, fromBranch: str) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    targetBranch = repo.get_branch(toBranch)
    originBranch = repo.get_branch(fromBranch)
    return repo.compare(targetBranch.commit.commit.sha, originBranch.commit.commit.sha)

def compareBranches(repo: Repository.Repository, toBranch: Branch.Branch, fromBranch: Branch.Branch) -> Comparison.Comparison:
    '''Comparies two branches within the same repo'''
    return repo.compare(toBranch.commit.commit.sha, fromBranch.commit.commit.sha)

# COMPARISON UTILS
def isAhead(comparison: Comparison.Comparison) -> bool:
    '''Branch is 1 or more commits ahead of target'''
    return comparison.ahead_by > 0

def isBehind(comparison: Comparison.Comparison) -> bool:
    '''Branch is 1 or more commits behind target'''
    return comparison.behind_by > 0
from github import Branch, Github
from datetime import date

from githubService.comparisonService import isAhead, compareBranches

def identifyEmptyBranches(gh: Github, repoFullName: str, targetBranch: str, daysStaleLimit: int = None) -> list[Branch.Branch]:
    '''Returns a list of branches that are empty (not ahead of target branch)'''
    emptyBranches = []
    repo = gh.get_repo(repoFullName)
    branches = repo.get_branches()
    target = repo.get_branch(targetBranch)

    for b in branches:
        if (not(isAhead(compareBranches(repo, target, b)))):
            if (daysStaleLimit != None):
                last_activity = date.fromisoformat(b.last_modified)
                delta = date.today - last_activity

                print("Last Modified: " + b.last_modified)
                print("Date Delta: " + delta.days)

                if (delta.days > daysStaleLimit):
                    emptyBranches.append(b)
            else:
                emptyBranches.append(b)

    return emptyBranches
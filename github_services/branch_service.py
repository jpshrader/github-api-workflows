'''GitHub Branch Service'''
from github import Branch, Repository, Github, GitRef

from github_services.repo_service import get_repo_by_full_name

# GET BRANCHES
def get_branches(github: Github, repo_full_name: str) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    repo = get_branch_from_repo(github, repo_full_name)
    return get_branches_by_repo(repo)

def get_branches_by_repo(repo: Repository.Repository) -> list[Branch.Branch]:
    '''Returns all branches of a given repo'''
    return repo.get_branches()

# GET BRANCH
def get_branch(github: Github, repo_full_name: str, branch_name: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return get_branch_from_repo(repo, branch_name)

def get_branch_from_repo(repo: Repository.Repository, branch_name: str) -> Branch.Branch:
    '''Returns a given branch of a given repo'''
    return repo.get_branch(branch_name)

def get_branch_from_list(branches: list[Branch.Branch], branch_name: str) -> Branch.Branch | None:
    '''Returns a given branch in a list of branches'''
    for branch in branches:
        if branch.name == branch_name:
            return branch
    return None

# DELETE BRANCH
def delete_branch(github: Github, repo_full_name: str, branch_name: str) -> None:
    '''Deletes a given branch of a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    ref = repo.get_git_ref(repo, f"heads/{branch_name}")
    ref.delete()

def delete_branch_from_repo(repo: Repository.Repository, branch_name: str) -> None:
    '''Deletes a given branch of a given repo'''
    ref = repo.get_git_ref(f"heads/{branch_name}")
    ref.delete()

def delete_branch_from_repo_by_branch(repo: Repository.Repository, branch: Branch.Branch) -> None:
    '''Deletes a given branch of a given repo'''
    ref = repo.get_git_ref(f"heads/{branch.name}")
    ref.delete()

# CREATE BRANCH
def create_branch(github: Github, repo_full_name: str, origin_branch_name: str, new_branch_name: str) -> GitRef.GitRef:
    '''Creates a branch on a given origin on a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    branch = get_branch_from_repo(repo, origin_branch_name)
    return repo.create_git_ref(new_branch_name, branch.commit.sha)

def create_branch_from_repo(repo: Repository.Repository, origin_branch_name: str, new_branch_name: str) -> GitRef.GitRef:
    '''Creates a branch on a given origin on a given repo'''
    branch = get_branch_from_repo(repo, origin_branch_name)
    return repo.create_git_ref(new_branch_name, branch.commit.sha)

def create_branch_from_repo_and_branch(repo: Repository.Repository, origin_branch: Branch.Branch, new_branch_name: str) -> GitRef.GitRef:
    '''Creates a branch on a given origin on a given repo'''
    return repo.create_git_ref(new_branch_name, origin_branch.commit.sha)

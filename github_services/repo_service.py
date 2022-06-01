'''GitHub Repository Service'''
from github import Repository, Github

# GET REPOS
def get_user_repos(github: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user owns'''
    owned_repos = []
    user = github.get_user()
    repos = user.get_repos()

    for repo in repos:
        if repo.owner.id == user.id:
            owned_repos.append(repo)

    return owned_repos

def get_org_repos(github: Github, org_name: str) -> list[Repository.Repository]:
    '''Returns all repos that the given organization owns'''
    return github.get_organization(org_name).get_repos()

def get_org_repo(github: Github, org_name: str, repo_name: str) -> Repository.Repository:
    '''Returns all repos that the given organization owns'''
    return github.get_organization(org_name).get_repo(repo_name)

def get_all_repos(github: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user has access to'''
    return github.get_user().get_repos()

# GET REPO
def get_repo_by_full_name(github: Github, repo_full_name: str) -> Repository.Repository:
    '''Returns a repo by its full name (ex. "{owner}/{repo}"'''
    return github.get_repo(repo_full_name)

# DELETE REPO
def delete_repo_by_full_name(github: Github, repo_full_name: str) -> None:
    '''Deletes a given repo by its full name'''
    delete_repo(get_repo_by_full_name(github, repo_full_name))

def delete_repo(repo: Repository.Repository) -> None:
    '''Deletes a given repo'''
    repo.delete()

from github import Repository, Github

def getAllRepos(gh: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user has access to.'''
    return gh.get_user().get_repos()

def getUserRepos(gh: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user owns.'''
    ownedRepos = []
    user = gh.get_user()
    repos = user.get_repos()

    for r in repos:
        if (r.owner.id == user.id):
            ownedRepos.append(r)

    return ownedRepos

def getOrgRepos(gh: Github, owner: str) -> list[Repository.Repository]:
    '''Returns all repos that the given organization owns.'''
    return gh.get_organization(owner).get_repos()

def getRepoByFullName(gh: Github, repoName: str) -> Repository.Repository:
    '''Returns a repo by its full name (ex. "{owner}/{slug}"'''
    return gh.get_repo(repoName)
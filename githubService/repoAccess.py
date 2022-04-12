from github import Repository, Github

def getAllRepos(githubAccess: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user has access to.'''
    return githubAccess.get_user().get_repos()

def getUserRepos(githubAccess: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user owns.'''
    ownedRepos = []
    user = githubAccess.get_user()
    repos = user.get_repos()

    for r in repos:
        if (r.owner.id == user.id):
            ownedRepos.append(r)

    return ownedRepos

def getOrgRepos(githubAccess: Github, owner: str) -> list[Repository.Repository]:
    '''Returns all repos that the given organization owns.'''
    return githubAccess.get_organization(owner).get_repos()

def getOrgRepo(githubAccess: Github, owner: str, repoName: str) -> Repository.Repository:
    '''Returns all repos that the given organization owns.'''
    return githubAccess.get_organization(owner).get_repo(repoName)

def getRepoByFullName(githubAccess: Github, repoName: str) -> Repository.Repository:
    '''Returns a repo by its full name (ex. "{owner}/{repoName}"'''
    return githubAccess.get_repo(repoName)

def deleteRepo(githubAccess: Github, repoName: str):
    githubAccess.get_repo(repoName).delete()
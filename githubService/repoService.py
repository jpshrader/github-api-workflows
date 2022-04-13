from github import Repository, Github

# GET USER REPOS
def getUserRepos(gh: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user owns'''
    ownedRepos = []
    user = gh.get_user()
    repos = user.get_repos()

    for r in repos:
        if (r.owner.id == user.id):
            ownedRepos.append(r)

    return ownedRepos

# GET ORG REPOS
def getOrgRepos(gh: Github, orgName: str) -> list[Repository.Repository]:
    '''Returns all repos that the given organization owns'''
    return gh.get_organization(orgName).get_repos()

def getOrgRepo(gh: Github, orgName: str, repoName: str) -> Repository.Repository:
    '''Returns all repos that the given organization owns'''
    return gh.get_organization(orgName).get_repo(repoName)

# GET REPOS
def getAllRepos(gh: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user has access to'''
    return gh.get_user().get_repos()

def getRepoByFullName(gh: Github, repoFullName: str) -> Repository.Repository:
    '''Returns a repo by its full name (ex. "{owner}/{repo}"'''
    return gh.get_repo(repoFullName)

# DELETE REPO
def deleteRepo(gh: Github, repoFullName: str):
    '''Deletes a given repo by its full name'''
    gh.get_repo(repoFullName).delete()
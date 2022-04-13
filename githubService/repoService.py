from github import Repository, Github

# GET USER REPOS
def getUserRepos(githubService: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user owns'''
    ownedRepos = []
    user = githubService.get_user()
    repos = user.get_repos()

    for r in repos:
        if (r.owner.id == user.id):
            ownedRepos.append(r)

    return ownedRepos

# GET ORG REPOS
def getOrgRepos(githubService: Github, orgName: str) -> list[Repository.Repository]:
    '''Returns all repos that the given organization owns'''
    return githubService.get_organization(orgName).get_repos()

def getOrgRepo(githubService: Github, orgName: str, repoName: str) -> Repository.Repository:
    '''Returns all repos that the given organization owns'''
    return githubService.get_organization(orgName).get_repo(repoName)

# GET REPOS
def getAllRepos(githubService: Github) -> list[Repository.Repository]:
    '''Returns all repos that the current user has access to'''
    return githubService.get_user().get_repos()

def getRepoByFullName(githubService: Github, repoFullName: str) -> Repository.Repository:
    '''Returns a repo by its full name (ex. "{owner}/{repo}"'''
    return githubService.get_repo(repoFullName)

# DELETE REPO
def deleteRepo(githubService: Github, repoFullName: str):
    '''Deletes a given repo by its full name'''
    githubService.get_repo(repoFullName).delete()
from github import PullRequest, PullRequestMergeStatus, Repository, Github

# GET PR
def getPullRequests(githubAccess: Github, repoName: str) -> list[PullRequest.PullRequest]:
    '''Returns all pull requests of a given repo'''
    return githubAccess.get_repo(repoName).get_pulls()

def getPullRequest(githubAccess: Github, repoName: str, prId: str) -> PullRequest.PullRequest:
    '''Returns a given pull request of a given repo'''
    return githubAccess.get_repo(repoName).get_pull(prId)

# MERGE PR
def mergePullRequest(githubAccess: Github, repoName: str, prId: str) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request of a given repo'''
    return getPullRequest(githubAccess, repoName, prId).merge()

def mergePullRequest(pullRequest: PullRequest.PullRequest) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request'''
    return pullRequest.merge()

# CLOSE PR
def closePullRequest(pullRequest: PullRequest.PullRequest):
    '''Closes a given pull request'''
    pullRequest.state = "closed"
    pullRequest.edit()

# CREATE PR
def createPullRequest(githubAccess: Github, repoName: str, title: str, body: str, toRef: str, fromRef: str) -> PullRequest.PullRequest:
    return githubAccess.get_repo(repoName).create_pull(title, body, base=toRef, head=fromRef, draft=False)

def createPullRequest(repo: Repository.Repository, title: str, body: str, toRef: str, fromRef: str) -> PullRequest.PullRequest:
    return repo.create_pull(title, body, base=toRef, head=fromRef, draft=False)

def createDraftPullRequest(githubAccess: Github, repoName: str, title: str, body: str, toBranch: str, fromBranch: str) -> PullRequest.PullRequest:
    githubAccess.get_repo(repoName).create_pull(title, body, base=toBranch, head=fromBranch, draft=True)

def createDraftPullRequest(repo: Repository.Repository, title: str, body: str, toBranch: str, fromBranch: str) -> PullRequest.PullRequest:
    return repo.create_pull(title, body, base=toBranch, head=fromBranch, draft=True)
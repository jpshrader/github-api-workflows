from github import PullRequest, PullRequestMergeStatus, Repository, Github

from githubService.repoService import getRepoByFullName

# GET PR
def getPullRequests(gh: Github, repoFullName: str) -> list[PullRequest.PullRequest]:
    '''Returns all pull requests of a given repo'''
    return getPullRequestsFromRepo(getRepoByFullName(gh, repoFullName))

def getPullRequest(gh: Github, repoFullName: str, prId: int) -> PullRequest.PullRequest:
    '''Returns a given pull request of a given repo'''
    return getPullRequestFromRepo(getRepoByFullName(gh, repoFullName), prId)

def getPullRequestsFromRepo(repo: Repository.Repository) -> list[PullRequest.PullRequest]:
    '''Returns all pull requests of a given repo'''
    return repo.get_pulls()

def getPullRequestFromRepo(repo: Repository.Repository, prId: int) -> PullRequest.PullRequest:
    '''Returns a given pull request of a given repo'''
    return repo.get_pull(prId)

# MERGE PR
def mergePullRequestByRepo(gh: Github, repoFullName: str, prId: int) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request of a given repo'''
    return mergePullRequest(getPullRequest(gh, repoFullName, prId))

def mergePullRequestByRepo(repo: Repository.Repository, prId: int) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request of a given repo'''
    return mergePullRequest(getPullRequestFromRepo(repo, prId))

def mergePullRequest(pullRequest: PullRequest.PullRequest) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request'''
    return pullRequest.merge()

# CLOSE PR
def closePullRequest(pullRequest: PullRequest.PullRequest):
    '''Closes a given pull request'''
    pullRequest.state = "closed"
    pullRequest.edit()

def closePullRequestByRepo(repo: Repository.Repository, prId: int):
    '''Closes a given pull request'''
    pullRequest = getPullRequest(repo, prId)
    closePullRequest(pullRequest)

def closePullRequestByName(gh: Github, repoFullName: str, prId: int):
    '''Closes a given pull request'''
    pullRequest = getPullRequest(gh, repoFullName, prId)
    closePullRequest(pullRequest)

# CREATE PR
def createPullRequest(gh: Github, repoFullName: str, title: str, body: str, toBranch: str, fromBranch: str, isDraft: bool) -> PullRequest.PullRequest:
    '''Creates a Pull Request between two refs (ex. 'head/main')'''
    repo = gh.get_repo(repoFullName)
    return createPullRequestByRepo(repo, title, body, toBranch, fromBranch, isDraft)

def createPullRequestByRepo(repo: Repository.Repository, title: str, body: str, toBranch: str, fromBranch: str, isDraft: bool) -> PullRequest.PullRequest:
    '''Creates a Pull Request between two refs (ex. 'head/main')'''
    return repo.create_pull(title, body, base=toBranch, head=fromBranch, draft=isDraft)
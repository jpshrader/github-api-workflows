from github import PullRequest, PullRequestMergeStatus, Repository, Github

# GET PR
def getPullRequests(gh: Github, repoFullName: str) -> list[PullRequest.PullRequest]:
    '''Returns all pull requests of a given repo'''
    return gh.get_repo(repoFullName).get_pulls()

def getPullRequest(gh: Github, repoFullName: str, prId: str) -> PullRequest.PullRequest:
    '''Returns a given pull request of a given repo'''
    return gh.get_repo(repoFullName).get_pull(prId)

# MERGE PR
def mergePullRequest(gh: Github, repoFullName: str, prId: str) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request of a given repo'''
    return getPullRequest(gh, repoFullName, prId).merge()

def mergePullRequest(pullRequest: PullRequest.PullRequest) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request'''
    return pullRequest.merge()

# CLOSE PR
def closePullRequest(pullRequest: PullRequest.PullRequest):
    '''Closes a given pull request'''
    pullRequest.state = "closed"
    pullRequest.edit()

# CREATE PR
def createPullRequest(gh: Github, repoFullName: str, title: str, body: str, toBranch: str, fromBranch: str, isDraft: bool) -> PullRequest.PullRequest:
    '''Creates a Pull Request between two refs (ex. 'head/main')'''
    return gh.get_repo(repoFullName).create_pull(title, body, base=toBranch, head=fromBranch, draft=isDraft)

def createPullRequest(repo: Repository.Repository, title: str, body: str, toBranch: str, fromBranch: str, isDraft: bool) -> PullRequest.PullRequest:
    '''Creates a Pull Request between two refs (ex. 'head/main')'''
    return repo.create_pull(title, body, base=toBranch, head=fromBranch, draft=isDraft)
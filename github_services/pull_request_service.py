'''GitHub Pull Request Service'''
from github import PullRequest, PullRequestMergeStatus, Repository, Github

from github_services.repo_service import get_repo_by_full_name

# GET PR
def get_pull_requests(github: Github, repo_full_name: str) -> list[PullRequest.PullRequest]:
    '''Returns all pull requests of a given repo'''
    return get_pull_requests_from_repo(get_repo_by_full_name(github, repo_full_name))

def get_pull_request(github: Github, repo_full_name: str, pr_id: int) -> PullRequest.PullRequest:
    '''Returns a given pull request of a given repo'''
    return get_pull_request_from_repo(get_repo_by_full_name(github, repo_full_name), pr_id)

def get_pull_requests_from_repo(repo: Repository.Repository) -> list[PullRequest.PullRequest]:
    '''Returns all pull requests of a given repo'''
    return repo.get_pulls()

def get_pull_request_from_repo(repo: Repository.Repository, pr_id: int) -> PullRequest.PullRequest:
    '''Returns a given pull request of a given repo'''
    return repo.get_pull(pr_id)

# MERGE PR
def merge_pull_request_by_repo_full_name(github: Github, repo_full_name: str, pr_id: int) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request of a given repo'''
    return merge_pull_request(get_pull_request(github, repo_full_name, pr_id))

def merge_pull_request_by_repo(repo: Repository.Repository, pr_id: int) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request of a given repo'''
    return merge_pull_request(get_pull_request_from_repo(repo, pr_id))

def merge_pull_request(pull_request: PullRequest.PullRequest) -> PullRequestMergeStatus.PullRequestMergeStatus:
    '''Merges a given pull request'''
    return pull_request.merge()

# CLOSE PR
def close_pull_request(pull_request: PullRequest.PullRequest) -> None:
    '''Closes a given pull request'''
    pull_request.state = "closed"
    pull_request.edit()

def close_pull_request_by_repo(repo: Repository.Repository, pr_id: int) -> None:
    '''Closes a given pull request'''
    pull_request = get_pull_request_from_repo(repo, pr_id)
    close_pull_request(pull_request)

def close_pull_request_by_name(github: Github, repo_full_name: str, pr_id: int) -> None:
    '''Closes a given pull request'''
    pull_request = get_pull_request(github, repo_full_name, pr_id)
    close_pull_request(pull_request)

# CREATE PR
def create_pull_request(github: Github, repo_full_name: str, title: str, body: str, to_branch_ref: str, from_branch_ref: str, is_draft: bool) -> PullRequest.PullRequest:
    '''Creates a Pull Request between two refs (ex. 'refs/heads/main')'''
    repo = github.get_repo(repo_full_name)
    return create_pull_request_by_repo(repo, title, body, to_branch_ref, from_branch_ref, is_draft)

def create_pull_request_by_repo(repo: Repository.Repository, title: str, body: str, to_branch_ref: str, from_branch_ref: str, is_draft: bool) -> PullRequest.PullRequest:
    '''Creates a Pull Request between two refs (ex. 'refs/heads/main')'''
    print(f'to: {to_branch_ref}')
    print(f'from: {from_branch_ref}')
    return repo.create_pull(title, body, base=to_branch_ref, head=from_branch_ref, draft=is_draft)

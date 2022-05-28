'''GitHub File Service'''
from github import ContentFile, Repository, Commit, Github

from repo_service import get_repo_by_full_name

# GET FILES
def get_files(github: Github, repo_full_name: str, path: str) -> list[ContentFile.ContentFile] | ContentFile.ContentFile:
    '''Returns file(s) at a given path in a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return get_files_in_repo(repo, path)

def get_files_in_repo(repo: Repository.Repository, path: str) -> list[ContentFile.ContentFile] | ContentFile.ContentFile:
    '''Returns file(s) at a given path in a given repo'''
    return repo.get_contents(path)

# CREATE FILE
def create_file(github: Github, repo_full_name: str, path: str, content: str, commit_message: str, branch_name: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Creates a file with given content at a given path in a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return create_file_in_repo(repo, path, content, commit_message, branch_name)

def create_file_in_repo(repo: Repository.Repository, path: str, content: str, commit_message: str, branch_name: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Creates a file with given content at a given path in a given repo'''
    return repo.create_file(path, commit_message, content, branch_name)

# UPDATE FILE
def update_file(github: Github, repo_full_name: str, path: str, content: str, commit_message: str, target_hash: str, branch_name: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Updates a file with given content at a given path in a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return update_file_in_repo(repo, path, content, commit_message, target_hash, branch_name)

def update_file_in_repo(repo: Repository.Repository, path: str, content: str, commit_message: str, target_hash: str, branch_name: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Updates a file with given content at a given path in a given repo'''
    return repo.update_file(path, commit_message, content, target_hash, branch_name)

# DELETE FILE
def delete_file(github: Github, repo_full_name: str, path: str, commit_message: str, target_hash: str, branch_name: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Deletes a file at a given path in a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return delete_file_in_repo(repo, path, commit_message, target_hash, branch_name)

def delete_file_in_repo(repo: Repository.Repository, path: str, commit_message: str, target_hash: str, branch_name: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Deletes a file at a given path in a given repo'''
    return repo.delete_file(path, commit_message, target_hash, branch_name)

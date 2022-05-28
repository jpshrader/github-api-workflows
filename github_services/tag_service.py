'''GitHub Tag Service'''
from github import Tag, GitTag, Repository, Github

from github_services.repo_service import get_repo_by_full_name

# GET TAGS
def get_tags(github: Github, repo_full_name: str) -> list[Tag.Tag]:
    '''Returns all tags on a given repo'''
    return get_tags_from_repo(get_repo_by_full_name(github, repo_full_name))

def get_tags_from_repo(repo: Repository.Repository) -> list[Tag.Tag]:
    '''Returns all tags on a given repo'''
    return repo.get_tags()

# CREATE TAG
def create_tag(github: Github, repo_full_name: str, tag_name: str, tag_message: str, commit_hash: str, tag_type: str) -> GitTag.GitTag:
    '''Creates a tag on a given repo - 'tag_type'= oneOf{ 'commit', 'tree', 'blob' }'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return create_tag_on_repo(repo, tag_name, tag_message, commit_hash, tag_type)

def create_tag_on_repo(repo: Repository.Repository, tag_name: str, tag_message: str, commit_hash: str, tag_type: str) -> GitTag.GitTag:
    '''Creates a tag on a given repo - 'tag_type'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag(tag_name, tag_message, commit_hash, tag_type)

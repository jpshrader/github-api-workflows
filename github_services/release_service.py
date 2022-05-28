'''GitHub Release Service'''
from github import GitRelease, Tag, GitTag, Repository, Github

from github_services.repo_service import get_repo_by_full_name

# GET RELEASES
def get_releases(github: Github, repo_full_name: str) -> list[GitRelease.GitRelease]:
    '''Returns all releases on a given repo'''
    return get_repo_by_full_name(github, repo_full_name).get_releases()

def get_releases_from_repo(repo: Repository.Repository) -> list[GitRelease.GitRelease]:
    '''Returns all releases on a given repo'''
    return repo.get_releases()

# GET RELEASE
def get_release(github: Github, repo_full_name: str, release_id: int) -> list[GitRelease.GitRelease]:
    '''Returns a release on a given repo'''
    return get_repo_by_full_name(github, repo_full_name).get_release(release_id)

def get_release_from_repo(repo: Repository.Repository, release_id: int) -> list[GitRelease.GitRelease]:
    '''Returns a release on a given repo'''
    return repo.get_release(release_id)

# CREATE RELEASE
def create_release(github: Github, repo_full_name: str, tag_name: str, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return create_release_on_repo(repo, tag_name, release_name, release_message, is_pre_release, is_draft)

def create_release_on_repo(repo: Repository.Repository, tag_name: str, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag_name, release_name, release_message, draft=is_draft, prerelease=is_pre_release)

def create_release_on_git_tag(github: Github, repo_full_name: str, tag: GitTag.GitTag, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return get_repo_by_full_name(github, repo_full_name).create_git_release(tag.tag, release_name, release_message, draft=is_draft, prerelease=is_pre_release)

def create_release_on_repo_and_git_tag(repo: Repository.Repository, tag: GitTag.GitTag, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag.tag, release_name, release_message, draft=is_draft, prerelease=is_pre_release)

def create_release_on_tag(github: Github, repo_full_name: str, tag: Tag.Tag, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return get_repo_by_full_name(github, repo_full_name).create_git_release(tag.name, release_name, release_message, draft=is_draft, prerelease=is_pre_release)

def create_release_on_repo_and_tag(repo: Repository.Repository, tag: Tag.Tag, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag.name, release_name, release_message, draft=is_draft, prerelease=is_pre_release)

# CREATE TAG AND RELEASE
def create_tag_and_release(github: Github, repo_full_name: str, tag_name: str, tag_message: str, commit_hash: str, tag_type: str, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tag_type'= oneOf{ 'commit', 'tree', 'blob' }'''
    return get_repo_by_full_name(github, repo_full_name).create_git_tag_and_release(tag_name, tag_message, release_name, release_message, commit_hash, tag_type, draft=is_draft, prerelease=is_pre_release)

def create_tag_and_release_on_repo(repo: Repository.Repository, tag_name: str, tag_message: str, commit_hash: str, tag_type: str, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tag_type'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag_and_release(tag_name, tag_message, release_name, release_message, commit_hash, tag_type, draft=is_draft, prerelease=is_pre_release)

def create_tag_and_release_on_repo_and_tag(repo: Repository.Repository, tag: Tag.Tag, tag_message: str, commit_hash: str, tag_type: str, release_name: str, release_message: str, is_pre_release: str, is_draft: bool) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tag_type'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag_and_release(tag.name, tag_message, release_name, release_message, commit_hash, tag_type, draft=is_draft, prerelease=is_pre_release)

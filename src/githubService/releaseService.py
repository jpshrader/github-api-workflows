from github import GitRelease, Tag, GitTag, Repository, Github

# GET RELEASES
def getReleases(gh: Github, repoFullName: str) -> list[GitRelease.GitRelease]:
    '''Returns all releases on a given repo'''
    return gh.get_repo(repoFullName).get_releases()

def getReleases(repo: Repository.Repository) -> list[GitRelease.GitRelease]:
    '''Returns all releases on a given repo'''
    return repo.get_releases()

# GET RELEASE
def getRelease(gh: Github, repoFullName: str, releaseId: int) -> list[GitRelease.GitRelease]:
    '''Returns a release on a given repo'''
    return gh.get_repo(repoFullName).get_release(releaseId)

def getRelease(repo: Repository.Repository, releaseId: int) -> list[GitRelease.GitRelease]:
    '''Returns a release on a given repo'''
    return repo.get_release(releaseId)

# CREATE RELEASE
def createRelease(gh: Github, repoFullName: str, tagName: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return gh.get_repo(repoFullName).create_git_release(tagName, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createRelease(repo: Repository.Repository, tagName: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tagName, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createRelease(gh: Github, repoFullName: str, tag: GitTag.GitTag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return gh.get_repo(repoFullName).create_git_release(tag.tag, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createRelease(repo: Repository.Repository, tag: GitTag.GitTag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag.tag, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createRelease(gh: Github, repoFullName: str, tag: Tag.Tag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return gh.get_repo(repoFullName).create_git_release(tag.name, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createRelease(repo: Repository.Repository, tag: Tag.Tag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag.name, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

# CREATE TAG AND RELEASE
def createTagAndRelease(gh: Github, repoFullName: str, tagName: str, tagMessage: str, commitHash: str, tagType: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return gh.get_repo(repoFullName).create_git_tag_and_release(tagName, tagMessage, releaseName, releaseMessage, commitHash, tagType, draft=isDraft, prerelease=isPreRelease)

def createTagAndRelease(repo: Repository.Repository, tagName: str, tagMessage: str, commitHash: str, tagType: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: str) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag_and_release(tagName, tagMessage, releaseName, releaseMessage, commitHash, tagType, draft=isDraft, prerelease=isPreRelease)
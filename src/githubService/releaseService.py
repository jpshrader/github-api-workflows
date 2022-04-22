from github import GitRelease, Tag, GitTag, Repository, Github

from githubService.repoService import getRepoByFullName

# GET RELEASES
def getReleases(gh: Github, repoFullName: str) -> list[GitRelease.GitRelease]:
    '''Returns all releases on a given repo'''
    return getRepoByFullName(gh, repoFullName).get_releases()

def getReleasesFromRepo(repo: Repository.Repository) -> list[GitRelease.GitRelease]:
    '''Returns all releases on a given repo'''
    return repo.get_releases()

# GET RELEASE
def getRelease(gh: Github, repoFullName: str, releaseId: int) -> list[GitRelease.GitRelease]:
    '''Returns a release on a given repo'''
    return getRepoByFullName(gh, repoFullName).get_release(releaseId)

def getReleaseFromRepo(repo: Repository.Repository, releaseId: int) -> list[GitRelease.GitRelease]:
    '''Returns a release on a given repo'''
    return repo.get_release(releaseId)

# CREATE RELEASE
def createRelease(gh: Github, repoFullName: str, tagName: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return createReleaseOnRepo(repo, tagName, releaseName, releaseMessage, isPreRelease, isDraft)

def createReleaseOnRepo(repo: Repository.Repository, tagName: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tagName, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createReleaseOnGitTag(gh: Github, repoFullName: str, tag: GitTag.GitTag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return getRepoByFullName(gh, repoFullName).create_git_release(tag.tag, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createReleaseOnRepoAndGitTag(repo: Repository.Repository, tag: GitTag.GitTag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag.tag, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createReleaseOnTag(gh: Github, repoFullName: str, tag: Tag.Tag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return getRepoByFullName(gh, repoFullName).create_git_release(tag.name, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

def createReleaseOnRepoAndTag(repo: Repository.Repository, tag: Tag.Tag, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release on a given repo'''
    return repo.create_git_release(tag.name, releaseName, releaseMessage, draft=isDraft, prerelease=isPreRelease)

# CREATE TAG AND RELEASE
def createTagAndRelease(gh: Github, repoFullName: str, tagName: str, tagMessage: str, commitHash: str, tagType: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return getRepoByFullName(gh, repoFullName).create_git_tag_and_release(tagName, tagMessage, releaseName, releaseMessage, commitHash, tagType, draft=isDraft, prerelease=isPreRelease)

def createTagAndReleaseOnRepo(repo: Repository.Repository, tagName: str, tagMessage: str, commitHash: str, tagType: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag_and_release(tagName, tagMessage, releaseName, releaseMessage, commitHash, tagType, draft=isDraft, prerelease=isPreRelease)

def createTagAndReleaseOnRepoAndTag(repo: Repository.Repository, tag: Tag.Tag, tagMessage: str, commitHash: str, tagType: str, releaseName: str, releaseMessage: str, isPreRelease: str, isDraft: bool) -> GitRelease.GitRelease:
    '''Creates a release with a corresponding tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag_and_release(tag.name, tagMessage, releaseName, releaseMessage, commitHash, tagType, draft=isDraft, prerelease=isPreRelease)
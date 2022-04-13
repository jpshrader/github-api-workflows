from github import Tag, GitTag, Repository, Github

# GET TAGS
def getTags(gh: Github, repoFullName: str) -> list[Tag.Tag]:
    '''Returns all tags on a given repo'''
    return gh.get_repo(repoFullName).get_tags()

def getTags(repo: Repository.Repository) -> list[Tag.Tag]:
    '''Returns all tags on a given repo'''
    return repo.get_tags()

# CREATE TAG
def createTag(gh: Github, repoFullName: str, tagName: str, tagMessage: str, commitHash: str, tagType: str) -> GitTag.GitTag:
    '''Creates a tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return gh.get_repo(repoFullName).create_git_tag(tagName, tagMessage, commitHash, tagType)

def getTag(repo: Repository.Repository, tagName: str, tagMessage: str, commitHash: str, tagType: str) -> GitTag.GitTag:
    '''Creates a tag on a given repo - 'tagType'= oneOf{ 'commit', 'tree', 'blob' }'''
    return repo.create_git_tag(tagName, tagMessage, commitHash, tagType)
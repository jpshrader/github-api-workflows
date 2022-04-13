from github import ContentFile, Repository, Commit, Github

# GET FILES
def getFiles(gh: Github, repoFullName: str, path: str) -> list[ContentFile.ContentFile] | ContentFile.ContentFile:
    '''Returns file(s) at a given path in a given repo'''
    return gh.get_repo(repoFullName).get_contents(path)

def getFiles(repo: Repository.Repository, path: str) -> list[ContentFile.ContentFile] | ContentFile.ContentFile:
    '''Returns file(s) at a given path in a given repo'''
    return repo.get_contents(path)

# CREATE FILE
def createFile(gh: Github, repoFullName: str, path: str, content: str, commitMessage: str, branchName: str) -> dict[str, ContentFile | Commit]:
    '''Creates a file with given content at a given path in a given repo'''
    return gh.get_repo(repoFullName).create_file(path, commitMessage, content, branchName)

def createFile(repo: Repository.Repository, path: str, content: str, commitMessage: str, branchName: str) -> dict[str, ContentFile | Commit]:
    '''Creates a file with given content at a given path in a given repo'''
    return repo.create_file(path, commitMessage, content, branchName)

# UPDATE FILE
def updateFile(gh: Github, repoFullName: str, path: str, content: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile | Commit]:
    '''Updates a file with given content at a given path in a given repo'''
    return gh.get_repo(repoFullName).update_file(path, commitMessage, content, targetHash, branchName)

def updateFile(repo: Repository.Repository, path: str, content: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile | Commit]:
    '''Updates a file with given content at a given path in a given repo'''
    return repo.update_file(path, commitMessage, content, targetHash, branchName)

# DELETE FILE
def deleteFile(gh: Github, repoFullName: str, path: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile | Commit]:
    '''Deletes a file at a given path in a given repo'''
    return gh.get_repo(repoFullName).delete_file(path, commitMessage, targetHash, branchName)

def deleteFile(repo: Repository.Repository, path: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile | Commit]:
    '''Deletes a file at a given path in a given repo'''
    return repo.delete_file(path, commitMessage, targetHash, branchName)

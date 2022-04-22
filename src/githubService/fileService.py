from github import ContentFile, Repository, Commit, Github

from githubService.repoService import getRepoByFullName

# GET FILES
def getFiles(gh: Github, repoFullName: str, path: str) -> list[ContentFile.ContentFile] | ContentFile.ContentFile:
    '''Returns file(s) at a given path in a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return getFilesInRepo(repo, path)

def getFilesInRepo(repo: Repository.Repository, path: str) -> list[ContentFile.ContentFile] | ContentFile.ContentFile:
    '''Returns file(s) at a given path in a given repo'''
    return repo.get_contents(path)

# CREATE FILE
def createFile(gh: Github, repoFullName: str, path: str, content: str, commitMessage: str, branchName: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Creates a file with given content at a given path in a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return createFileInRepo(repo, path, commitMessage, content, branchName)

def createFileInRepo(repo: Repository.Repository, path: str, content: str, commitMessage: str, branchName: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Creates a file with given content at a given path in a given repo'''
    return repo.create_file(path, commitMessage, content, branchName)

# UPDATE FILE
def updateFile(gh: Github, repoFullName: str, path: str, content: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Updates a file with given content at a given path in a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return updateFileInRepo(repo, path, commitMessage, content, targetHash, branchName)

def updateFileInRepo(repo: Repository.Repository, path: str, content: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Updates a file with given content at a given path in a given repo'''
    return repo.update_file(path, commitMessage, content, targetHash, branchName)

# DELETE FILE
def deleteFile(gh: Github, repoFullName: str, path: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Deletes a file at a given path in a given repo'''
    repo = getRepoByFullName(gh, repoFullName)
    return deleteFileInRepo(repo, path, commitMessage, targetHash, branchName)

def deleteFileInRepo(repo: Repository.Repository, path: str, commitMessage: str, targetHash: str, branchName: str) -> dict[str, ContentFile.ContentFile | Commit.Commit]:
    '''Deletes a file at a given path in a given repo'''
    return repo.delete_file(path, commitMessage, targetHash, branchName)

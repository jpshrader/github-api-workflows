'''GitHub Label Service'''
from github import Label, Repository, Github

from github_services.repo_service import get_repo_by_full_name

# GET LABELS
def get_labels(github: Github, repo_full_name: str) -> list[Label.Label]:
    '''Returns all labels from a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return get_labels_from_repo(repo)

def get_labels_from_repo(repo: Repository.Repository) -> list[Label.Label]:
    '''Returns all labels from a given repo'''
    return repo.get_labels()

# GET LABEL
def get_label(github: Github, repo_full_name: str, label_name: str) -> Label.Label:
    '''Returns a label from a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return get_label_from_repo(repo, label_name)

def get_label_from_repo(repo: Repository.Repository, label_name: str) -> Label.Label:
    '''Returns a label from a given repo'''
    return repo.get_label(label_name)

# CREATE LABEL
def create_label(github: Github, repo_full_name: str, label_name: str, label_color: str, label_description: str) -> Label.Label:
    '''Creates a label in a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    return create_label_from_repo(repo, label_name, label_color, label_description)

def create_label_from_repo(repo: Repository.Repository, label_name: str, label_color: str, label_description: str) -> Label.Label:
    '''Creates a label in a given repo'''
    return repo.create_label(label_name, label_color, label_description)

# UPDATE LABEL
def update_label(github: Github, repo_full_name: str, label_name: str, label_color: str, label_description: str) -> bool:
    '''Updates a given label in a given repo'''
    repo = get_repo_by_full_name(github, repo_full_name)
    label = repo.get_label(label_name)
    return update_label_from_repo(label, label_color, label_description)

def update_label_from_repo(label: Label.Label, label_color: str, label_description: str) -> bool:
    '''Updates a given label'''
    label.color = label_color
    label.description = label_description
    return label.update()

'''GitHub User Service'''

from github import Github, AuthenticatedUser, NamedUser

def get_current_user(github: Github) -> AuthenticatedUser.AuthenticatedUser:
    '''Returns the current authenticated user'''
    return github.get_user()

def get_user(github: Github, user_id) -> NamedUser.NamedUser:
    '''Returns the current authenticated user'''
    return github.get_user(user_id)

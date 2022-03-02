import github

def getUserRepos(githubAccess: github):
    return githubAccess.get_user().get_repos()
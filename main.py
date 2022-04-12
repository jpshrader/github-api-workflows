import json
import appSettingsConstants as constants
import githubService.repoAccess as repoAccess

from githubService.githubAccessFactory import getGitHubAccess

def getSettings():
    settingsFile = open(constants.SETTINGS_FILE)
    return json.load(settingsFile)

if __name__ == '__main__':
    settings = getSettings()
    githubAccess = getGitHubAccess(settings[constants.ACCESS_TOKEN], settings[constants.ITEMS_PER_PAGE])

    userRepos = repoAccess.getUserRepos(githubAccess)

    for r in userRepos:
        print(r.name)
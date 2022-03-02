import json
import appSettingsConstants as constants
import githubService.branchAccess as branchAccess
import githubService.repoAccess as repoAccess

from githubService.githubAccess import getGitHubAccess

def getSettings():
    settingsFile = open(constants.SETTINGS_FILE)
    return json.load(settingsFile)

if __name__ == '__main__':
    settings = getSettings()
    gh = getGitHubAccess(settings[constants.ACCESS_TOKEN], settings[constants.ITEMS_PER_PAGE])

    userRepos = repoAccess.getOrgRepos(gh)

    for r in userRepos:
        print(r.name)
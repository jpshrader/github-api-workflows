import github
from githubService.githubAccess import getGitHubAccess
import appSettingsConstants
import json

def getSettings():
    settingsFile = open(appSettingsConstants.SETTINGS_FILE)
    return json.load(settingsFile)

if __name__ == "__main__":
    settings = getSettings()

    githubAccess = getGitHubAccess(settings[appSettingsConstants.ACCESS_TOKEN])
import json
import appSettingsConstants as constants

from githubService.githubServiceFactory import getGithubService

def getSettings():
    settingsFile = open(constants.SETTINGS_FILE)
    return json.load(settingsFile)

if __name__ == '__main__':
    settings = getSettings()
    gh = getGithubService(settings[constants.ACCESS_TOKEN], settings[constants.ITEMS_PER_PAGE])
from .mongo import *


def getConfig():
    Config.find_one({'type': 'assetscan'})

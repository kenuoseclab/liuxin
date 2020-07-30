from .mongo import *


def getConfig():
    result = {}
    try:
        row_ini = Config.find_one({'type': 'assetscan'})
        if row_ini and 'config' in row_ini:
            for key in row_ini['config']:
                result[key] = row_ini['config'][key]['value']
    except Exception as e:
        print(e)
    return result


def getStatic():
    try:
        pass
    except Exception as e:
        print(e)


def monitor(configIni):
    while True:
        new_config = Config.find_one({'type': 'assetscan'})
        pass

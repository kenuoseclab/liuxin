from tools.mongo import *
import threading

if __name__ == '__main__':

    assetIni = Config.find_one({'type': 'assetscan'})
    print(assetIni)

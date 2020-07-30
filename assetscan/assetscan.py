import threading

from toolsLib.common import *

if __name__ == '__main__':
    # 获取配置文件
    configIni = getConfig()
    records = getRecord()
    # totalFlag = {"masscan": 0, "isScan": 0}
    # threading.Thread(target=monitor, args=(configIni,)).start()
    # while True:
    #     pass
    #     # 主循环

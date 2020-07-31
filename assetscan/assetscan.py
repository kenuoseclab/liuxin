import threading
from toolsLib.common import *

if __name__ == '__main__':
    # 获取配置文件
    configIni = getConfig()
    record = getRecord()
    totalFlag = {"masscan": 0, "isScan": 0}
    threading.Thread(target=monitor, args=(configIni, record, totalFlag)).start()
    threading.Thread(target=cursor, args=()).start()
    # while True:
    #     pass
    #     # 主循环

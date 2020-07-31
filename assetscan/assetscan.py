import threading
from toolsLib.common import *

if __name__ == '__main__':
    # 获取配置文件
    configIni = getConfig()
    record = getRecord()
    totalFlag = {"masscan": 0, "isScan": 0, 'progress': 0}
    threading.Thread(target=monitor, args=(configIni, record, totalFlag)).start()
    threading.Thread(target=check, args=(record, totalFlag)).start()
    print(threading.active_count())
    # while True:
    #     try:
    #         if () or totalFlag['isScan']:
    #             pass
    #     except Exception as e:
    #         print(e)

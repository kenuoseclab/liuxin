import threading
from toolsLib.common import *
from toolsLib.log import logWrite
from toolsLib.start import *

if __name__ == '__main__':
    # 获取配置文件
    configIni = getConfig()
    logWrite("获取配置成功")
    record = getRecord()
    logWrite('获取记录成功')
    totalFlag = {"masscan": 0, "isScan": 0, 'progress': 0}
    threading.Thread(target=monitor, args=(configIni, record, totalFlag)).start()
    threading.Thread(target=check, args=(record, totalFlag)).start()
    socket.setdefaulttimeout(int(configIni['timeout']) / 2)
    dateRunRecord = []
    while True:
        try:
            date = datetime.now()
            hour = date.hour
            day = date.day
            dateStr = date.strftime('%Y%m%d')
            cy_day, cy_hour = configIni['cycle'].split('|')
            if (dateStr not in dateRunRecord and hour == int(cy_hour) and day % int(cy_day) == 0) or totalFlag[
                'isScan']:
                totalFlag['isScan'] = 0
                dateRunRecord.append(dateStr)
                totalFlag['progress'] = 0
                logWrite("开始扫描")
                s = start(configIni)
                s.totalFlag = totalFlag
                s.record = record
                s.run()
        except Exception as e:
            print(e)
        time.sleep(30)

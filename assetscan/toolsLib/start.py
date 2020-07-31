from .tools import *
from IPy import IP
from .icmp import icmp
from plugin.masscan import run


class start():
    def __init__(self, configIni):
        self.configIni = configIni
        self.icmp = int(self.configIni['port_list'].split('|')[0])
        self.isMasscan = int(self.configIni['masscan'].split('|')[0])
        self.whiteList = self.configIni['white_list'].split('\n')

    def run(self):
        allIp = self.getAllIp()
        pingAllIp = set()
        ipPort = {}
        while True:
            if self.icmp and not pingAllIp:
                pingAllIp = self.icmpScan(allIp)
            elif self.isMasscan and not ipPort:
                if pingAllIp:
                    ipList = pingAllIp
                else:
                    ipList = allIp
                ipPort = self.masscan(ipList, self.configIni['masscan'].split('|')[1],
                                      self.configIni['masscan'].split('|')[2])
            else:
                self.scan()
                break

    def icmpScan(self, allIp):
        try:
            ping = icmp(allIp)
            return ping.run()
        except Exception as e:
            print('The current user permissions unable to send icmp packets')
            print(e)
            return allIp

    def masscan(self, ipList, path, rate):
        try:
            if len(ipList) == 0:
                return
            return run(ipList, path, rate)
        except Exception as e:
            print(e)
            print('No masscan plugin detected')

    def scan(self):
        return

    def getAllIp(self):
        allIp = set()
        try:
            row_ip_list = self.configIni['scan_list'].split('\n')
            for row_ip in row_ip_list:
                try:
                    if not row_ip:
                        continue
                    elif '-' in row_ip:
                        allIp.update(gen_ip(row_ip))
                    elif '/' in row_ip:
                        ipList = [str(x) for x in IP(row_ip)]
                        allIp.update(ipList[1:len(ipList) - 1])
                    else:
                        allIp.add(row_ip)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        return allIp - set(self.whiteList)

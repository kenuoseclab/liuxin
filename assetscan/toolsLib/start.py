from .tools import *
from IPy import IP
from .icmp import icmp


class start():
    def __init__(self, configIni):
        self.configIni = configIni
        self.icmp = int(self.configIni['port_list'].split('|')[0])
        self.masscan = int(self.configIni['masscan'].split('|')[0])
        self.whiteList = self.configIni['white_list'].split('\n')

    def run(self):
        allIp = self.getAllIp()
        pingAllIp = set()
        ipPort = {}
        while True:
            if self.icmp and not pingAllIp:
                pingAllIp = self.icmpScan(allIp)
            elif self.masscan and not ipPort:
                pass
            else:
                self.scan()
                break

    def icmpScan(self, allIp):
        try:
            ping = icmp(allIp)
            return ping.run()
        except Exception as e:
            print()
            print(e)
            return allIp

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

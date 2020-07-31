class start():
    def __init__(self, configIni):
        self.configIni = configIni
        self.icmp = int(self.configIni['port_list'].split('|')[0])
        self.masscan = int(self.configIni['masscan'].split('|')[0])
        self.whiteList = self.configIni['white_list'].split('\n')

    def run(self):
        allIp = self.getAllIp()
        for ip in allIp:
            while True:
                if self.icmp:
                    pass
                elif self.masscan:
                    pass
                else:
                    self.scan()

    def scan(self):
        pass

    def getAllIp(self):
        allIp = set()
        try:
            row_ip_list = self.configIni['scan_list'].split('\n')
            for row_ip in row_ip_list:
                try:
                    if not row_ip:
                        continue
                    elif '_' in row_ip:
                        pass
                    elif '/' in row_ip:
                        pass
                    else:
                        allIp.add(row_ip)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        return allIp - set(self.whiteList)

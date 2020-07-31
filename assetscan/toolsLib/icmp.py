import os
import struct
import array
import socket
import threading
import time
from .log import logWrite


class icmp():
    def __init__(self, allIp, timeout=3):
        self.timeout = timeout
        self.allIp = allIp
        self.__data = struct.pack('h', 1)
        self.__id = os.getpid()
        if self.__id >= 65535: self.__id = 65534

    def __checkSum(self, packet):
        shorts = array.array('H', packet)
        sum = 0
        for short in shorts:
            sum += short & 0xffff
        while (sum >> 16) > 0:
            sum = (sum & 0xffff) + (sum >> 16)
        return (~sum) & 0xffff

    @property
    def __icmpPacket(self):
        header = struct.pack('bbHHh', 8, 0, 0, self.__id, 0)
        packet = header + self.__data
        sum = self.__checkSum(packet)
        header = struct.pack('bbHHh', 8, 0, sum, self.__id, 0)
        return header + self.__data

    @property
    def __icmpSock(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(self.timeout)
        return sock

    def run(self):
        sock = self.__icmpSock
        packet = self.__icmpPacket
        recvFrom = set()
        t = threading.Thread(target=self.__send, args=(sock, self.allIp, packet))
        t.start()
        while True:
            try:
                ac_ip = sock.recvfrom(1024)[1][0]
                if ac_ip not in recvFrom:
                    logWrite('{} active'.format(ac_ip))
                    recvFrom.add(ac_ip)
            except Exception as e:
                print(e)
                pass
            finally:
                if not t.is_alive():
                    break
        return self.allIp & recvFrom

    def __send(self, sock, packet):
        for ip in self.allIp:
            try:
                sock.sendto(packet, (ip, 1))
            except Exception as e:
                print(e)
                pass
        time.sleep(self.timeout)

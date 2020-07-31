import os
import struct
import array
import socket


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
        pass
        return

    @property
    def __sock(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(self.timeout)
        return sock

    def run(self):
        return

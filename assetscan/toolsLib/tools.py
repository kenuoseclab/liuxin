# -*- coding: utf-8 -*-
def ip2num(ip):
    ips = [int(x) for x in ip.split('.')]
    return ips[0] << 24 | ips[1] << 16 | ips[2] << 8 | ips[3]


def removeSide(ip):
    if ip <= 0:
        ip = 1
    elif ip >= 255:
        ip = 254
    return ip


def num2ip(num):
    return '%s.%s.%s.%s' % (
        removeSide((num >> 24) & 0xff), (num >> 16) & 0xff, (num >> 8) & 0xff, removeSide((num & 0xff)))


def gen_ip(ip):
    start, end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start, end + 1) if num & 0xff]

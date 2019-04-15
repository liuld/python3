#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

# IPy - 用于处理IPv4和IPv6地址和网络的类和工具.
# IP('8.8.8.8').iptype()                   地址类型: 'PUBLIC'/'PRIVATE'
# IP('8.8.8.8').version()                  ip版本: 4/6
# IP('192.168.0.0/24').len()               网段的IP个数
# IP('192.168.0.0/24').reverseName()       反向解析地址格式(str)
# IP('192.168.0.0/24').reverseNames()      反向解析地址格式(列表格式)
# print(IP('192.168.0.0/24').net())        网段
# print(IP('192.168.0.0/24').netmask())    掩码
# print(IP('192.168.0.0/24').prefixlen())  掩码，INT型
# print(IP('192.168.0.0/24').strNormal(0)) 网段
# print(IP('192.168.0.0/24').strNormal(1)) 网段/prefixlen
# print(IP('192.168.0.0/24').strNormal(2)) 网段/掩码
# print(IP('192.168.0.0/24').strNormal(3)) 192.168.0.0-192.168.0.255
# print(IP('192.168.0.0/24').strNetmask()) 掩码
# print(IP('192.168.0.1').strBin())        转换为二进制格式
# print(IP('192.168.0.1').strHex())        转换为16进制格式

from IPy import IP
import sys

if len(sys.argv) == 2:
    ip_s = sys.argv[1]
else:
    print("usage: %s ip[/netmask]" % sys.argv[0])
    exit(1)
try:
    ips = IP(ip_s)
except Exception as e:
    print("\033[1;31merror\033[0m: %s" % e)
    exit(1)
if ips.len() > 1:
    print("%27s\t%s" % ("\033[1;32mnet:\033[0m", ips.net()))
    print("%27s\t%s" % ("\033[1;32mnetmask:\033[0m", ips.netmask()))
    print("%27s\t%s" % ("\033[1;32mbroadcast:\033[0m", ips.broadcast()))
    print("%27s\t%s" % ("\033[1;32mreverse address:\033[0m", ips.reverseNames()[0]))
    print("%24s\t%d" % ("\033[1;32m可用ip数:\033[0m", (ips.len()-2)))
    print("%27s\t%s" % ("\033[1;32mip range:\033[0m", ips.strNormal(3)))
else:
    print("\033[1;32mip: %s\niptype: %s\nbinary ip: %s\nreverse address: %s\033[0m" % (ips.strFullsize(), ips.iptype(), ips.strBin(), ips.reverseNames()[0]))

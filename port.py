#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
banner = """
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

İNSTAGRAM : CODEWİTHLUKA
WEB SİTE : LUKACODER.COM
------------------------------------
Usage -: python2 port.py <ip> 
                                                                                                   """
print(banner)
if ( len(sys.argv) != 2 ):
    print "Usage: " + sys.argv[0] + " you must enter IP or FQDN as argument"
    sys.exit(1)

remote_host = sys.argv[1]

for remote_port in [21,22,23,80,139,139,389,443,445,3128,3306,3389]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(20)
        try:
                sock.connect((remote_host, remote_port))
        except Exception,e:
                print "%d closed " % remote_port
        else:
                print "%d open" % remote_port
        sock.close()

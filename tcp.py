#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
BUFF = 1024
HOST = ''
PORT = 65534
ADDRESS = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.STREAM)

def tcpServer(host, port):
    try:
        print "please wating connection......"
        sock.connect(ADDRESS)
    except Exception as e:
        print " %s erros!" % e
    try:
        data_recv = sock.recv(BUFF)
        print "recvfrom %s data..." % data_recv
    except Exception as e:
        print "%s errors!" % e
        
def main():
    pass
        
        
        
        
if __name__ == '__main__':
    main()

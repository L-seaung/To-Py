#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
BUFF = 1024
HOST = ''
PORT = 65534

sock = socket.socket(socket.AF_INET, socket.STREAM)

def tcpServer(host, port):
    try:
        sock.connect((HOST, PORT))
        

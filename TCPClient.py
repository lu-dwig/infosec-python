#!/usr/bin/python3

import socket

#Create socket object
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '192.168.1.104'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.1.104', port)) #You can substitue the host with the server IP


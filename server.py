#!/usr/bin/env python

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() #Host is the server IP
port = 444 #Port to listen on 

    
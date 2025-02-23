#!/usr/bin/env python

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#The host should be a string ' 127.0.0.1 '
#host = "ip of the machine running / virtual machine"
host = socket.gethostname() #Host is the server IP
port = 444 #Port to listen on 

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection 
    clientsocket,address = serversocket.accept()

    print("received connection from " % str(address))
    
    #Message sent to client after successful connection
    message = 'hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message)

    clientsocket.close()   
#!/usr/bin/python2
import socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=raw_input("enter the message: ")
x.sendto(msg,("127.0.0.1",9999))
while 4>2:
    data=x.recvfrom(1000)
    print "message from client: ",data[0]
    print "ip address: ",data[1][0]

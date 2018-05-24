#!/usr/bin/python2
import socket,time
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("127.0.0.1",9999))
while 4>2:
  data=x.recvfrom(1000)
  print "message from client: ",data[0]
  print "ip address: ",data[1][0]
  time.sleep(1)
  reply=raw_input("plz type your reply: ")
  x.sendto(reply,data[1])

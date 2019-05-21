#!/usr/bin/python3 
import socket 
ip="13.232.68.231"
port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4 > 3:
           msg=input("enter the msg :")
           n=msg.encode('ascii')
           s.sendto(n,(ip,port))

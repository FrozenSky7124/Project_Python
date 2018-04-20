# -*- coding:utf-8 -*- #

from socket import *

tcpClientSocket = socket(AF_INET, SOCK_STREAM)

serAddr = ("192.168.1.112", 17124)
tcpClientSocket.connect(serAddr)

tcpClientSocket.send("TestTCP!".encode("gb2312"))

recvData = tcpClientSocket.recv(1024)

print("RecvData:%s"%recvData)

tcpClientSocket.close()
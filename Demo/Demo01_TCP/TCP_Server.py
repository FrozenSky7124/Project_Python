# -*- coding:utf-8 -*- #

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", 17124))
serverSocket.listen(5) # 设置套接字为被动，监听数量限制
clientSocket, clientInfo = serverSocket.accept() # 接收请求并建立TCP连接

recvData = clientSocket.recv(1024)

print("[%s]:%s"%(str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()

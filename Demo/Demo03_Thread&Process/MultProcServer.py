# -*- coding:utf-8 -*- #

from socket import *
from multiprocessing import *
from time import sleep

def clientProcFunc(newSocket, destAddr):
	while True:
		recvData = newSocket.recv(1024)
		if len(recvData) > 0:
			print("      SubProcess Receive: [%s]:%s      "%(str(destAddr), recvData))
		else 
			print("      SubProcess Close  : [%s]      "%str(destAddr))
			break
	newSocket.close()

def main():

	serSocket = socket(AF_INET, SOCK_STREAM)
	serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 设置Socket可以重复使用端口
	localAddr = ("", 17124)
	serSocket.bind(localAddr)
	serSocket.listen(5)

	try:
		while True:
			print("----- MainProcess ONLINE -----")
			newSocket, destAddr = serSocket.accept()
			print("----- MainProcess NewProcess:[%s] -----"%str(destAddr))
			client = Process(target = clientProcFunc, args=(newSocket, destAddr))
			client.start()

			# 因为子进程中已经传递了newSocket的引用，所以父进程将关闭newSocket
			newSocket.close()
	finally:
		serSocket.close()

if __name__ == '__main__':
	main()
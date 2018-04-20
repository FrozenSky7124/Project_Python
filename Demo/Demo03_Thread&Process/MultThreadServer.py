# -*- coding:utf-8 -*- #

from socket import *
from threading import Thread
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
			client = Thread(target = clientProcFunc, args=(newSocket, destAddr))
			client.start()

			# 因为线程中共享程序空间中的newSocket 所以不能在主线程中调用close方法
			# newSocket.close()
	finally:
		serSocket.close()

if __name__ == '__main__':
	main()
# -*- coding:utf-8 -*- #

import struct
from socket import *
import time
import os

def main():


	# 获取要下载的文件名:
	downloadFileName = raw_input("请输入要下载的文件名:")	

	# 创建Socket
	udpSocket = socket(AF_INET, SOCK_DGRAM)

	# 封装tftp协议请求包 详见tftp协议文档
	requestFileData = struct.pack("!H%dsb5sb"%len(downloadFileName), 1, downloadFileName, 0, "octet", 0)

	# 发送下载文件的请求
	udpSocket.sendto(requestFileData, ("192.168.1.113", 69))

	# 预创建文件来接收数据
	f = open(downloadFileName, "w")
	
	num = 0 # 接收到的数据包序号
	flag = True # 表示能够下载数据，如果为false将删除预创建的文件

	while True:
		# 接收服务器发送回来的应答数据
		responseData = udpSocket.recvfrom(1024)

		recvData, serverInfo = responseData

		# 解包获得状态码和数据包序号
		opNum = struct.unpack("!H", recvData[:2])
		packetNum = struct.unpack("!H", recvData[2:4])

		print(packetNum[0])

		# 如果服务器发送过来的是文件的内容的话:
		if opNum[0] == 3: # 因为opNum此时是一个元组(3,)，所以需要使用下标来提取某个数据
			
			# 计算出这次应该接收到的数据包序号，应该是上一次接收到的值的基础上+1
			num = num + 1

			# 如果一个下载的文件特别大，即接收到的数据包序号超过了2Byte
			# 那么会从0继续开始，所以这里需要判断，如果超过了65535，改为0
			if num == 65536:
				num = 0

			# 判断这次接收到的数据包序号是否是上一次的数据包+1
			# 如果是才会写入到文件中，否则不能写入（因为会重复）
			if num == packetNum[0]:
				# 把收到的数据写入到文件中
				f.write(recvData[4:])
				num = packetNum[0]

			# 封装ACK包 并回复
			ackData = struct.pack("!HH", 4, packetNum[0])
			udpSocket.sendto(ackData, serverInfo)

		elif opNum[0] == 5:
			print("未找到该文件！")
			flag = False

		if len(recvData) < 516:
			break

	if flag == True:
		f.close()
	else:
		# 未能传输数据 删除预创建的文件
		os.unlink(downloadFileName)

if __name__ == '__main__':
	main()

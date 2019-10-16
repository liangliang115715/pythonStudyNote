#_author: 
#date:

import socket

sk=socket.socket()

adress=("127.0.0.1",8000)
sk.connect(adress)
# 接收
# data=sk.recv(1024)
# print(str(data,"utf8"))
# 发送
while True:
	inp=input(">>:")
	if not inp or inp=="exit":
		break
	sk.send(bytes(inp,"utf8"))
	size_data=int(str(sk.recv(1024),"utf8"))
	print(size_data)
	data=bytes()
	while len(data) != size_data:
		data+=sk.recv(1024)
	# print(str(data, "gbk"))
	print(str(data, "utf8"))
sk.close()
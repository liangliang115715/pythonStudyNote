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
	data=sk.recv(1024)
	print(str(data,"utf8"))
sk.close()
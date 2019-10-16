#_author: 
#date:


import socket

ip_port = ('127.0.0.1', 8009)
sk = socket.socket()
sk.connect(ip_port)

print("客户端启动：")
while True:
	inp = input("please input>>:")
	if inp == 'exit':
		break
	else:
		sk.sendall(bytes(inp,"utf8"))
	data = sk.recv(1024)
	print(str(data,"utf8"))
sk.close()
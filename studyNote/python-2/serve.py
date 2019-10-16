#_author: 
#date:


import socket
# 创建socket对象
sk=socket.socket()
# 为socket对象提供ip地址和端口，然后绑定
adress=("127.0.0.1",8000)

sk.bind(adress)
# 监听设置端口 等待客户端的请求
sk.listen(2)

# accept阻塞，等待客户端连接
# inp=input(">>:")
# conn.send(bytes(inp,"utf8"))
# 此处的conn指的就是客户端的socket对象即客户端定义的sk=socket.socket（）中的sk
while True:
	print("waiting.....")
	conn, addr = sk.accept()
	print(addr)
	while True:
		try:
			data=conn.recv(1024)
		except Exception:
			break
		if not data:
			break
		print(str(data,"utf8"))
		inp=input(">>:")
		conn.send(bytes(inp,"utf8"))

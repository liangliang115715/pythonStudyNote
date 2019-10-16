
import socket

import select

sk=socket.socket()
sk.bind(("127.0.0.1",9004))
sk.listen(5)
inputs=[sk,]
while True:
	r,w,e=select.select(inputs,[],[],5)
	for i in r:
		if i == sk:
			conn,add=i.accept()
			input()
			inputs.append(conn)
			print(inputs)
		else:
			data_byte=i.recv(1024)
			print(str(data_byte,"utf8"))
			inp=input("回答%s号客户>>:")
			i.sendall(bytes(inp,"utf8"))
	print(">>>>>>")

	
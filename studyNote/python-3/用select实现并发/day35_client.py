#_author: Administrator
#date:  
"呦，又在写bug呐！！！"

import socket

sk=socket.socket()

sk.connect(("127.0.0.1",9004))

while True:
	inp=input(">>".strip())
	sk.send(inp.encode("utf8"))
	data=sk.recv(1024)
	print(data.decode("utf8"))
	
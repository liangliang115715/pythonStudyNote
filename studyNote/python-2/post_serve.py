#_author: 
#date:

import socket
import os


sk = socket.socket()
adress = ("127.0.0.1", 8000)
sk.bind(adress)
sk.listen(2)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
while True:
	print("waiting.....")
	conn, addr = sk.accept()
	while True:
		data=conn.recv(1024)
		cmd,filename,file_size=str(data,"utf8").split("|")
		path=os.path.join(BASE_DIR,"yuan",filename)
		file_size=int(file_size)
		f = open(path, "ab")
		has_receive = 0
		while has_receive != file_size:
			data = conn.recv(1024)
			f.write(data)
			has_receive += len(data)
		f.close()
		print("加载成功")
#_author: 
#date:

import socket
import os

sk=socket.socket()
adress=("127.0.0.1",8000)
sk.connect(adress)

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
while True:
	inp=input(">>:").strip()
	
	cmd,path=inp.split("|")
	
	path=os.path.join(BASE_DIR,path)
	filename=os.path.basename(path)
	file_size=os.stat(path).st_size # 返回int型数据
	file_info="post|%s|%s"%(filename,file_size)
	sk.sendall(bytes(file_info,"utf8"))
	
	f=open(path,"rb")
	has_sent=0
	while has_sent!=file_size:
		data=f.read(1024)
		sk.sendall(data)
		has_sent+=len(data)
	f.close()
	print("上传结束")
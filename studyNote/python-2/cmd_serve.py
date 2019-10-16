#_author: 
#date:

import socket
import subprocess
# 创建socket对象
sk=socket.socket()
# 为socket对象提供ip地址和端口，然后绑定
adress=("127.0.0.1",8000)
sk.bind(adress)
# 监听设置端口 等待客户端的请求
sk.listen(2)


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
		# 将子进程转到主进程，并将执行结果存入obj对象内
		obj=subprocess.Popen(str(data,"utf8"),shell=True,stdout=subprocess.PIPE)
		# obj对象内存储的执行结果读出
		cmd_result=obj.stdout.read()
		
		result_len=bytes(str(len(cmd_result)),"utf8")
		conn.sendall(result_len)
		conn.sendall(cmd_result)
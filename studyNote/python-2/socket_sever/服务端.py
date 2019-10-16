#_author: 
#date:
import socketserver

class MySever(socketserver.BaseRequestHandler):
	def handle(self):
		print("服务器端启动")
		while True:
			conn = self.request
			print(self.client_address)
			while True:
				data = conn.recv(1024)
				print(str(data, "utf8"))
				conn.sendall(data)
			conn.close()
if __name__=="__main__":
	server=socketserver.ThreadingTCPServer(("127.0.0.1",8009),MySever)
	server.serve_forever()
		

			
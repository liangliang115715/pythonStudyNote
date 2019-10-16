#_author: 
#date:
f=open("xx","r+",encoding="utf8")
num=0
for line in f:
	num+=1
	if num==3:
		f.write("alex")
	print(line)
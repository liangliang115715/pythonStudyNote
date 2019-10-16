#_author: Administrator
#date:  
"呦，又在写bug呐！！！"



def f(x,l=[]):
	for i in range(x):
		l.append(i**2)
	print(l)


f(2)
f(3,[3,2,1])
f(3)
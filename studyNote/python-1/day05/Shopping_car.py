salary=int(input("please input your salary:"))
shopping_list=["1.iphone 6s  $5800","2.mac book  $9000","3.coffee  $32","4.python book $ 80","5.biycle $1500"]
print("this is the shopping list:")
for i in range (4):
	print(shopping_list[i])
price=[0,5800,9000,32,80,1500]
shopping_car=[]
need=0
count=0
quit = "n"

while quit == "n" :
	print("you have %d rest,what do you want to buy?"%salary)
	
	print(shopping_list)
	
	need = int(input("the number of things' you want to buy:"))
	
	salary = salary - price[need]
	if salary > 0:
		shopping_car.append(shopping_list[need-1])
		print(shopping_list[need-1],"have already jion your shopping car")
		count+=1
		
	else:
		print("it is still %d far away :"%(-salary))
		quit=input("do you want quit?[y/n]:")
print("shopping list:")
for j in range (count-1):
	print(shopping_list[j])
print("your rest money is %d"%(salary+price[need]))
print("welcome your next coming!!!")

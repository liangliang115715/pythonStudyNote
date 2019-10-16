#_author: 
#date:

dict_list={
	         "A_sheng":{
		         "a_shi":("a1_xian","a2_xian","a3_xian"),
	         },
	         "B_sheng":{
		         "b_shi":("b1_xian","b2_xian","b3_xian")
	         },
	         "C_sheng":{
		         "c_shi":("c1_xian","c2_xian","c3_xian"),
	         },
}
layer=dict_list
recover=[]
count=1
quit = False

while not quit:
	for key in layer:
		print(key)
	choice=input("请输入你要详细查看的地方。【退出/返回：q/b】").strip()
	if len(choice)==0:continue
	print(layer)
	if choice in layer:
		recover.append(layer)
		layer = layer[choice]
		# count+=1
		# if count %3==0:
		# 	print("这是最底层：")
	elif choice=="q":
		quit=True
	elif choice=="b":
		# if count==1:
		layer=recover.pop()
	else:
		print("无此项")

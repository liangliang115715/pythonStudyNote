#_author: 
#date:
import sys
import os

def show_menu():
	print(menu_info)

def delete(user_enter):
	del_layer = input("please input the layer you want delete:")
	if del_layer in user_enter:
		del user_enter[del_layer]
	else:
		print("查无此项")

def add_key(user_enter, count):
	add_part = input("请输入你要在此添加的内容：")
	if add_part in user_enter:
		print("已存在该项")
	# 底层标志用count并不准确
	elif count == 3:
		user_enter[add_part] = None
		print("已添加至最底层")
	else:
		user_enter[add_part] = {}

def revise(user_enter):
	key_revise = input("请输入你要修改的内容：")
	if key_revise in user_enter:
		revised_key = input("请输入变更后的内容")
		user_enter[revised_key] = user_enter.pop(key_revise)
	else:
		print("查无此项！！！")

menu_info="1.删除 2.添加 3.修改 4.退出"

# 打开文档并转化为字典模式遍历输出***************************************************
f = open("三级菜单", "r+", encoding="utf-8")
dict_f=eval(f.read().strip())
layer=dict_f
recover=[]
count=0
# 查看主循环----------------------------------------------------
while True:
	for key in layer:
		print(key)
	count+=1
	show_menu()
	choice=input("please input the place you want to see[返回：b]:")
	if len(choice)==0:continue
	if choice in layer:
		recover.append(layer)
		layer=layer[choice]
	elif choice=="1":
		delete(layer)
		f.close()
	elif choice=="2":
		add_key(layer,count)
		f.close()
	elif choice=="3":
		revise(layer)
		f.close()
	elif choice=="4":
		f.close()
		break
	elif choice=="b":
		if count==1:
			print("已经是最顶层！！！")
			continue
		layer=recover.pop()
		count-=1
	else:print("无此项，请重新输入！")

#_author: 
#date:
import time
#闭包 ：在内部函数中引用外部变量（非全局变量），
    #   那么这个内部函数就叫闭包
start=time.time()
def outer():
	x=10
	def inner():#条件1：内部函数inner
		print(x)#条件2： 对外部环境的一个变量进行引用
	return inner#结论： 此内部函数inner即为一个闭包
f=outer()
print(f)   # 这一步中 f=inner 即f与inner共同存储同一个地址
f()         # 附加： 局部变量，全局无法调用
end=time.time()
#闭包总结：闭包=函数块（inner）+定义时的环境（环境：x=10）
print("%s"%(end-start))
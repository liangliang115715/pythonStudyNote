from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.


def index(request):

    return render(request,"index.html")

#表记录添加
def addbook(request):
    #方式一
    # b=Book(name="python base",price=99,author="ll",pub_data="2019-1-31")
    # b.save()

    #方式二
    Book.objects.create(name="老男孩linux",price=78,author="oldboy",pub_data="2016-12-12")

    return HttpResponse("添加成功")

#表记录修改
def update(request):
    #方式一：
    b=Book.objects.get(author="oldboy")
    b.price=120
    b.save()

    #方式二：
    # Book.objects.filter(author="ll").update(price=899)

    return HttpResponse("修改成功!")
#表记录删除
def delete(request):

    Book.objects.filter(author="oldboy").delete()

    return HttpResponse("删除成功！")


def select(request):

    # 单表查询

    # book_list=Book.objects.all()
    # 可切片
    # book_list=Book.objects.all()[::2]
    # book_list=Book.objects.all()[::-1]
    # 通过键来查找
    # book_list=Book.objects.filter(id=2)#结果为一个集合，可迭代
    # book_list=Book.objects.get(id=2)#只能取出一条记录，不可迭代

    #first last  第一个 最后一个
    # book_list=Book.objects.first()
    # book_list=Book.objects.last()

    #查找对象的属性  ret1返回字典  ret2返回 值的元组
    # ret1=Book.objects.filter(author="yuan").values("name","price")
    # ret2=Book.objects.filter(author="yuan").values_list("name","price")
    # print(ret1)#{'price': 45, 'name': 'PHP'}
    # print(ret2)#('PHP', 45)

    #exculde  包含与所给筛选条件不匹配的对象  返回一个对象集合
    # ret3 = Book.objects.exclude(author="yuan").values_list("name", "price")
    # print(ret3)

    #distinct 去重
    # ret4=Book.objects.all().values("name").distinct()
    # print(ret4)

    #count 计数
    # ret5=Book.objects.all().count()
    # print(ret5)


    #万能的双下划线 __  ： 模糊匹配
    # gt :>  lt: <     contains :包含  icontains: 包含（不区分大小写） ...
    # ret6=Book.objects.filter(price__gt=50).values("name","price")
    # ret7=Book.objects.filter(name__icontains="p").values("name","price")
    #
    # print(ret6)
    # print(ret7)

    # return render(request,"index.html",{"book_list":book_list})


    # 多表查询
    #方式一
    # book_obj=Book.objects.get(name="python")
    # print(book_obj.publish.name)
    # print(book_obj.Publish.place)
    # print(type(book_obj.Publish))

    #方式二
    pub_obj=Publish.objects.filter(name="人民出版社")[0]
    print(pub_obj.book_set.all().values("name","price"))
    # print(type(pub_obj.book_set))





    return render(request,"index.html")

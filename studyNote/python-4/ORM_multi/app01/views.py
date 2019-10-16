from django.shortcuts import render,HttpResponse


#引入聚合函数
from django.db.models import Avg,Max,Min,Sum,Count

#引入F、Q查询
from django.db.models import F,Q



# Create your views here.
from app01.models import *


# 多表操作
def index(request):

    return render(request,"index.html")

#表记录添加
def addbook(request):


    return HttpResponse("添加成功")

#表记录修改
def update(request):


    return HttpResponse("修改成功!")
#表记录删除
def delete(request):


    return HttpResponse("删除成功！")


def select(request):

    #查询方式三
    # 正向查找 此处publish为外键
    # ret1=Book.objects.filter(publish__name="人民出版社").values("name","price")
    # print(ret1)

    #反向查找  此处book为models中的类名
    # ret2=Publish.objects.filter(book__name="python").values("name")
    # print(ret2)

    # 练习
    # ret3=Book.objects.filter(name="python").values("publish__name")
    # print(ret3)
    # ret4=Book.objects.filter(publish__city="北京").values("name")
    # print(ret4)
    # ret5=Book.objects.filter(pub_date__gt="2017-7-1",pub_date__lt="2017-12-31").values("publish__name")
    # print(ret5)

    #多对多查询
    #正向查找
    # book_obj=Book.objects.get(id=3)
    # authors_book_obj=book_obj.authors.all()
    # print(authors_book_obj)
    #反向查找
    # authors_obj=Author.objects.get(id=2)
    # book_authors_obj=authors_obj.book_set.all()
    # print(book_authors_obj)



    return render(request,"index.html")



def addmuch(requset):
    # 一对多添加
    #方式一
    #Book.objects.create(name="liux运维",price=77,pub_date="2017-12-13",publish_id=2)

    #方式二
    # publish_obj=Publish.objects.filter(name="人民出版社")[0]
    # Book.objects.create(name="GO",price=23,pub_date="2017-12-16",publish=publish_obj)


    #多对多添加  为第三张自动生成的表添加数据 能通过语句
    #也能通过手动在models内添加类 在类中添加两个外键


    #为同一本书 绑定/解除 多个作者
    #book_obj=Book.objects.get(id=3)
    #authous_obj=Author.objects.all()

    #book_obj.authors.add(*authous_obj)
    #book_obj.authors.remove(*authous_obj)

    #聚合函数
    # ret1=Book.objects.all().aggregate(Avg("price"))
    # print(ret1)

    # ret2=Book.objects.filter(authors__name="alex").aggregate(Sum("price"))
    # print(ret2)

    #分组查询
    # ret3=Book.objects.values("authors__name").annotate(Sum("price"))
    # print(ret3)

    # ret4=Publish.objects.values("name").annotate(Min("book__price"))
    # print(ret4)

    #F、Q查询  可对筛选条件进行与或非 +-*等操作
    #所有book price+10
    # Book.objects.all().update(price=F("price")+10)

    # ret5=Book.objects.filter(Q(price=87)|Q(name="GO"))
    # print(ret5)

    #F,Q查询可与字段查询混合使用，但必须放在字段查询前面
    # ret6=Book.objects.filter(Q(name="GO"),price=33)
    # print(ret6)




    return HttpResponse("success!")
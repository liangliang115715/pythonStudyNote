from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app01.pager import Pagenation
# Create your views here.


class CustomPaginator(Paginator):
    def __init__(self,current_page,per_pagecount,*args,**kwargs):
        self.current_page=current_page
        self.per_pagecount=per_pagecount
        # super(CustomPaginator,self) 首先找到 CustomPaginator 的父类（就是类 Paginator），
        # 然后把类 CustomPaginator的对象self转换为类 Paginator 的对象
        super(CustomPaginator,self).__init__ (*args,**kwargs)
    def page_num_range(self):
        # 总页数小于设置的显示页数
        if self.num_pages<self.per_pagecount:
            return range(1,self.num_pages+1)
        #取显示页数的中间数
        part=self.per_pagecount//2
        #当前页码小于一半时
        if self.current_page<=part:
            return  range(1,self.per_pagecount+1)
        #当前页码+part大于总页数
        if(self.current_page+part)>self.num_pages:
            return range(self.num_pages-self.per_pagecount+1,self.num_pages+1)
        #一般情况
        return range(self.current_page-part,self.current_page+part+1)





USER_LIST=[]
for i in range(1,999):
    temp={"name":"root"+str(i),"age":i}
    USER_LIST.append(temp)


def index(request):
    current_page=int(request.GET.get("p"))
    per_pagecount=10
    start=(current_page-1)*per_pagecount
    end=current_page*per_pagecount
    data=USER_LIST[start:end]
    return render(request,"index.html",{"user_list":data})


def index1(request):

    current_page = int(request.GET.get("p"))
    paginator=CustomPaginator(current_page,7,USER_LIST,10)

    try:
        posts=paginator.page(current_page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,"index1.html",{"posts":posts})



def index2(request):
    currentPage=request.GET.get("p")
    page_obj=Pagenation(999,currentPage)

    data_list=USER_LIST[page_obj.start():page_obj.end()]
    return render(request,"index2.html",{"data":data_list,"page_obj":page_obj})
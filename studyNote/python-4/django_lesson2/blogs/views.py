from django.shortcuts import render,HttpResponse
import time
# Create your views here.
def show_time(req):
    t=time.ctime()

    # return HttpResponse("time:%s"%t)
    return render(req,"show_time.html",{"time":t})


def query(req):
    dic={"name":"ll","age":21,"sex":"男"}
    a="<a href="">click</a>"
    return render(req,"index.html",locals())

def login(req):

    return HttpResponse("ok!")
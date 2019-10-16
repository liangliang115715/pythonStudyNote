from django.shortcuts import render,HttpResponse,redirect


import time
# Create your views here.

def show_time(req):

    t=time.ctime()
    return render(req,"show_time.html",{"time":t})

def index1(request,y):

    return HttpResponse("%s"%y)

def index2(request,year,month):

    return HttpResponse("year:%s  month:%s"%(year,month))


def register(request):


    if request.method=="POST":
        print(request.POST.get("user"))
        print(request.POST.get("age"))

        user=request.POST.get("user")
        if user=="ll":
            return redirect("/login/")

        return HttpResponse("success!")

    return render(request,"register.html")


def login(req):

    return render(req,"login.html")
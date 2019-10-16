from django.shortcuts import render,HttpResponse,redirect
import cookie_session
# Create your views here.


def login(request):

    if request.method=="POST":
        name=request.POST.get("user")
        pwd=request.POST.get("pwd")
        if name=="ll" and pwd=="123":
            # ret=redirect("/index/")
            # ret.set_cookie("username",name,max_age=10)#max_age 设置cookie最大存储时间

            request.session["is_login"]=True
            request.session["username"]=name


            # return ret
            return redirect("/index/")

    return render(request,"login.html")

def index(request):

    # if request.COOKIES.get("username",None):
    #     name=request.COOKIES.get("username",None)
    #     return render(request,"index.html",locals())
    if request.session.get("is_login",None):
        name=request.session.get("username")
        return render(request,"index.html",locals())
    else:
        return redirect("/login/")

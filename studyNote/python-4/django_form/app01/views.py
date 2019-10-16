from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from app01.forms import UserForms


def users(request):
    users_list=models.UserInfo.objects.all()
    return render(request,"users.html",{"users_list":users_list})

def add_user(request):
    if request.method=="GET":
        obj=UserForms()
        return render(request,"add_user.html",{"obj":obj})
    else:
        obj=UserForms(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect("users/")
        else:
            return render(request, "add_user.html", {"obj": obj})
def edit_user(request,nid):
    if request.method=="GET":
        data=models.UserInfo.objects.filter(id=nid).first()
        obj=UserForms({"username":data.username,"email":data.email})
        return render(request,"edit_user.html",{"obj":obj,"nid":nid})
    else:
        obj=UserForms(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect("users/")
        else:
            return render(request, "edit_user.html", {"obj": obj,"nid":nid})



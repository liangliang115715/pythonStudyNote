from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def get_classes(request):
    cls_list=models.Class.objects.all()
    return render(request,"get_classes.html",{"cls_list":cls_list})
def add_classes(request):
    if request.method=="GET":
        print("!!!!!!!!!!")
        return render(request,"add_classes.html")
    elif request.method=="POST":
        title=request.POST.get("title")
        models.Class.objects.create(title=title)
        return redirect("classes.html")
def del_classes(request):
    nid=request.GET.get("nid")
    models.Class.objects.filter(id=nid).delete()
    return redirect("classes.html")
def edit_classes(request):
    if request.method=="GET":
        nid=request.GET.get("nid")
        obj=models.Class.objects.filter(id=nid).first()
        return render(request,"edit_classes.html",{"obj":obj})
    if request.method=="POST":
        nid=request.GET.get("nid")
        title=request.POST.get("new_title")
        models.Class.objects.filter(id=nid).update(title=title)
        return redirect("classes.html")
from django.shortcuts import render,HttpResponse,redirect
from app01 import models



def get_students(request):

    stu_list=models.Student.objects.all()

    return render(request,"get_students.html",{"stu_list":stu_list})


def add_students(request):
    if request.method=="GET":
        cls_list=models.Class.objects.all()
        return render(request,"add_students.html",{"cls_list":cls_list})
    elif request.method=="POST":
        name=request.POST.get("user")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        cs=request.POST.get("cs")

        models.Student.objects.create(name=name,
                                      age=age,
                                      gender=gender,
                                      cs_id=cs
                                      )
        return redirect("students.html")


def del_students(request):
    nid=request.GET.get("nid")
    models.Student.objects.filter(id=nid).delete()
    return redirect("students.html")
def edit_students(request):
    if request.method=="GET":
        cls_list=models.Class.objects.all()
        nid = request.GET.get("nid")
        obj=models.Student.objects.filter(id=nid).first()
        return render(request,"edit_students.html",{"obj":obj,"cls_list":cls_list})
    elif request.method=="POST":
        nid=request.GET.get("nid")
        name=request.POST.get("new_name")
        age=request.POST.get("new_age")
        gender=request.POST.get("new_gender")
        cs=request.POST.get("new_cs")
        models.Student.objects.filter(id=nid).update(
            name=name,
            age=age,
            gender=gender,
            cs_id=cs
        )
        return redirect("students.html")

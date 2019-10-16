from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
# Create your views here.


def student(request):
    stu_list=models.Student.objects.all()
    cls_list=models.Class.objects.all()
    return render(request,"student.html",{"stu_list":stu_list,"cls_list":cls_list})

def add_student(request):
    response={"status":True,"message":None,"data":None}
    try:
        n=request.POST.get("name")
        a=request.POST.get("age")
        g=request.POST.get("gender")
        c=request.POST.get("cs_id")

        obj=models.Student.objects.create(
            name=n,
            age=a,
            gender=g,
            cs_id=c,
        )
        response["data"]=obj.id


    except Exception as e:
        response["status"]=False
        response["message"]="用户输入错误"
    result=json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

def del_student(request):
    response = {"status": True, "message": None, "data": None}
    try:
        nid=request.POST.get("delNid")
        obj=models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        response["status"]=False
        response["message"]=e
    result=json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

def edit_student(request):
    response={"status":True,"message":None,"data":None}
    try:
        id=request.POST.get("id")
        n=request.POST.get("name")
        a=request.POST.get("age")
        g=request.POST.get("gender")
        c=request.POST.get("cs_id")
        obj=models.Student.objects.filter(id=id).update(
            name=n,
            age=a,
            gender=g,
            cs_id=c,
        )
        # response["data"]=obj.id
        print(response,type(obj))


    except Exception as e:
        print(e)
        response["status"]=False
        response["message"]=e
    result=json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

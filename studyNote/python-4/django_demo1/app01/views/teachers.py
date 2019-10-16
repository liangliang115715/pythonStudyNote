from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def set_teachers(request):
    if request.method=="GET":
        nid=request.GET.get("nid")
        obj_cls=models.Class.objects.filter(id=nid).first()
        # obj_cls_teachers=obj_cls.m.all()
        #将班级对应的老师提取成id与name的元组形式：（id，name）
        obj_cls_teachers=obj_cls.m.all().values_list("id","name")
        all_teacher_list=models.Teacher.objects.all()
        # 3目运算 提取ID列表
        id_list=list(zip(*obj_cls_teachers))[0] if list(zip(*obj_cls_teachers)) else []
        print(id_list)
        return render(request,"set_teachers.html",
                      {" obj_cls_teachers": obj_cls_teachers,
                        "all_teacher_list":all_teacher_list,
                       "id_list":id_list,
                       "nid":nid,
                       }
                      )
    elif request.method=="POST":
        nid=request.GET.get("nid")
        new_teacher_ids=request.POST.getlist("new_teacher_ids")

        obj=models.Class.objects.filter(id=nid).first()
        obj.m.set(new_teacher_ids)
        return redirect("classes.html")
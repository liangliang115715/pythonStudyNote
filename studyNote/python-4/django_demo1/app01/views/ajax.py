from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def ajax1(request):
    nid=request.GET.get("nid")
    msg="成功"
    try:
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        msg=str(e)
    return HttpResponse(msg)
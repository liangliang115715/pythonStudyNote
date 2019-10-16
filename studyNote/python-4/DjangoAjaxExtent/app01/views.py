from django.shortcuts import render,HttpResponse,redirect
import json
# Create your views here.

def index(request):

    return render(request, "index.html")

def ajax1(request):
    response=request.POST
    # print(response,request.body)
    file=request.FILES
    print(file)
    # response=json.dumps(response)
    return HttpResponse(".....")

def ajax2(request):
    response1=request.POST
    # response2=request.body
    file=request.FILES
    print(file)
    # print(response1,type(response1))
    # print(response2,type(response2))
    return HttpResponse("ajax2 提交成功!")

def ajax3(request):
    response=request.POST
    file=request.FILES
    print(file)
    # print(response)
    return HttpResponse("ojbk!")

def ajax4(request):
    ret={"status":False,"message":None}
    print(request.POST)
    file=request.FILES.get("img2")
    f=open(file.name,"wb")
    for item in file.chunks():
        f.write(item)
    f.close()
    print(file)
    json.dumps(ret)
    return HttpResponse(ret)
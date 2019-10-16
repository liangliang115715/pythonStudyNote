from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def upload(request):
    if request.method == "GET":
        return render(request,"upload.html")
    else:
        user=request.POST.get("user")
        img_obj=request.FILES.get("img")

        f=open(img_obj.name,"wb")
        for line in img_obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse("上传成功")
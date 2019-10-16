from django.shortcuts import render,HttpResponse

# Create your views here.


def index(req):
	
	print ("get",req.GET)
	print("post",req.POST)
	
	print("files",req.FILES)
	
	for item in req.FILES:
		fileObj=req.FILES.get(item)
		f=open(fileObj.name,"wb")
		iter_file=fileObj.chunks()
		for line in iter_file:
			f.write(line)
		f.close()
	return HttpResponse("注册成功")
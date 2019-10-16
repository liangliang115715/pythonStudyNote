from django.shortcuts import render
from app01 import models
from django.http import JsonResponse

# Create your views here.
def index(request):
	
	newList=models.News.objects.all()
	imgList=models.HeadPhoto.objects.all()
	company=models.Companny.objects.all()
	classList=models.Classes.objects.all()
	studentList=models.StudentInfo.objects.all()
	return render(request, "index2.html",locals())

def mapPage(request):

	return render(request,"index3.html")

# def video(request,*args,**kwargs):
# 	conditions = {}
# 	for k,v in kwargs.items():
# 		temp=int(v)
# 		kwargs[k]=temp
# 		if temp:
# 			conditions[k]=int(v)
# 	dir_list=models.direction.objects.all()
# 	sub_list=models.subject.objects.all()
# 	grade_list=models.grade.objects.all()
#
# 	video_list=models.videos.objects.filter(**conditions)
# 	print(video_list.values())
# 	return render(request,"video.html",{
# 		"sub_list":sub_list,
# 		"grade_list":grade_list,
# 		"kwargs":kwargs,
# 		"video_list":video_list,
# 	})

def video(request,*args,**kwargs):
	conditions = {}
	for k,v in kwargs.items():
		temp=int(v)
		kwargs[k]=temp
	
	direct_id=kwargs.get("direct_id")
	subject_id=kwargs.get("subject_id")
	grade_id=int(kwargs.get("grade_id"))

	if direct_id == 0:
		sub_list = models.subject.objects.all()
		if subject_id == 0:
			pass
		else:
			conditions["subject_id"]=subject_id
	else:
		dir_obj=models.direction.objects.filter(id=direct_id).first()
		sub_list = dir_obj.subject.all()
		# print(sub_list)#<QuerySet [(1,), (3,)]>
		if sub_list:
			sub_list_id=sub_list.values_list("id")
			sub_list_ids = list(zip(*sub_list_id))[0]
			# print(sub_list_ids)#(1, 3)
		else:
			sub_list_ids = []
		if subject_id == 0:
			conditions["subject_id__in"]=sub_list_ids
		else:
			if subject_id in sub_list_ids:
				conditions["subject_id"]=subject_id
			else:
				conditions["subject_id__in"] = sub_list_ids
				kwargs["subject_id"] = 0
	if grade_id == 0:
		pass
	else:
		conditions["grade_id"]=grade_id
	
	
	direct_list=models.direction.objects.all()
	grade_list=models.grade.objects.all()
	video_list=models.videos.objects.filter(**conditions)
	
	return render(request, "video.html", {
		
		"direct_list":direct_list,
		"sub_list":sub_list,
		"grade_list":grade_list,
		"kwargs":kwargs,
		"video_list":video_list,
	})
	
	
def img(request):
	
	return render(request,"img.html")

def get_img(request):
	nid=request.GET.get("nid")
	img_list=models.imgs.objects.filter(id__gt=nid).values("id","src","title","img")
	img_list=list(img_list)
	ret={"status":True,"data":img_list}
	
	return JsonResponse(ret)
	
	
	
	
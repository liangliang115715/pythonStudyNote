from django.shortcuts import render

# Create your views here.


def backend(request):

    return render(request, "base.html")

def student(request):

    student_list=["志超","正文", "浩辰","邵晨" ]
    return render(request, "student.html", locals())




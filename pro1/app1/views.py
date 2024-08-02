from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm


# Create your views here.

def homeview(request):
    return render(request,"app1/home.html",{})

def addview(request):
    form = StudentForm()
    if request.method =="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})

def showview(request):
    obj =Student.objects.all()
    print(obj)
    return render(request,"app1/show.html",{"obj":obj})

def deleteview(request,x):
    obj = Student.objects.get(stu_id=x)
    obj.delete()
    return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"obj":obj})


def updateview(request,pk):
    obj=Student.objects.get(stu_id=pk)
    form =StudentForm(instance=obj)
    if request.method =="POST":
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})


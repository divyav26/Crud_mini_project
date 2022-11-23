from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Student
from .models import User
# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = Student(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name']
            c = fm.cleaned_data['uclass']
            d = fm.cleaned_data['div']
            r =fm.cleaned_data['rollno']
            e = fm.cleaned_data['email']
            cont = fm.cleaned_data['contact']
            reg = User(name=n,uclass = c,div=d,rollno=r,email=e,contact = cont)
            reg.save()
            fm = Student()

    else:
            fm = Student()
    stud = User.objects.all()
    return render(request,'add_show.html',{'fm':fm, 'stu':stud})


def delete(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm =Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = Student(instance=pi)
    return render(request,'update.html',{'form':fm})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
#About View
def student_list(request):
    data=Student.objects.all()#select * from Student
    print(data)#records fetched from student table
    return render(request,'students/student_list.html',{'data':data,'count':len(data)})

def student_form(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect('studentlist')
    else:
        form=StudentForm()
        return render(request, 'students/student_form.html',{'form':form})
def student_delete(request,sid):
    record=Student.objects.get(id=sid)
    record.delete()
    return redirect('studentlist')

def student_update(request,sid):
    record=Student.objects.get(id=sid)
    if request.method=="GET":
        form=StudentForm(instance = record)
        return render(request,'students/update_form.html',{'form':form})
    else:
        form=StudentForm(request.POST, instance=record)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect('studentlist')

# Create your views here.
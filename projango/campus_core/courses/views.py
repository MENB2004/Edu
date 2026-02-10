from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
# Create your views here.
def course_form(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect('coursedetails')
    else:
        form=CourseForm()
        return render(request, 'courses/course_form.html',{'form':form})

def course_details(request):
    details=Course.objects.all()
    print(details)
    return render(request, 'courses/course_details.html',{'details':details})

def course_delete(request,sid):
    record=Course.objects.get(id=sid)
    record.delete()
    return redirect('coursedetails')

@login_required
def course_update(request,sid):
    record=Course.objects.get(id=sid)
    if request.method=="GET":
        form=CourseForm(instance = record)
        return render(request,'courses/update_form.html',{'form':form})
    else:
        form=CourseForm(request.POST, instance=record)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect('coursedetails')
# Create your views here.
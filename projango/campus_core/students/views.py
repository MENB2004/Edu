from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h2> Campus Management System <h2/>")
#About View
def student_list(request):
    return render(request, 'students/student_list.html')
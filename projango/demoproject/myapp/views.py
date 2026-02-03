from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Home View
def student(request):
    return HttpResponse("<h2> Welcome to Student Directory <h2/>")
#About View
def course(request):
    return HttpResponse("<h2> Hello<h2/>")
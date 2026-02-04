from django.shortcuts import render
from django.http import HttpResponse
#About View
def student_list(request):
    
    stud_records=[{'slno':1,'name':'rahul','course':'cs','sem':3},{'slno':2,'name':'reena','course':'cs','sem':3}]

    data={'admission_closed':True,"count":63,'students':stud_records}

    return render(request, 'students/student_list.html',{'adm_data':data}) # type: ignore
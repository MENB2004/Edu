from django.db import models

# Create your models here.
class Student(models.Model):
    slno = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    course = models.CharField(max_length=50)
    
#student table with 4 coloumns of specified name and type will be created
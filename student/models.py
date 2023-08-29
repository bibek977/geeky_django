from django.db import models

class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    semail = models.CharField(max_length=100)
    spass = models.CharField(max_length=100)

    # after migrate have to give default value
    comment = models.CharField(max_length=50,default="not available")
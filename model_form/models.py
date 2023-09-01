from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    roll = models.IntegerField()


class Intern(models.Model):
    name = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    phone = models.IntegerField(default=9800000000)
    location = models.CharField(max_length=50)
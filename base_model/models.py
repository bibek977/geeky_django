from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class Student(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Intern(Student):
    program = models.CharField(max_length=200)

class Person(BaseModel):
    age = models.IntegerField()
    created_at = None

# It doesn't set to None
class Developer(Intern):
    address = None
    created_at = None

class AllInfo(Intern):
    age = models.IntegerField()
    college = models.CharField(max_length=200)

    class Meta:
        abstract = True

class NewDeveloper(AllInfo):
    age = None
    created_at = None
    address = None

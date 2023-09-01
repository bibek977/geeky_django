from django import forms
from .models import *

class StudentForm(forms.Form):
    name = forms.CharField()
    faculty = forms.CharField()
    roll = forms.IntegerField()


class InternForm(forms.ModelForm):

    program = forms.CharField(max_length=50)

    class Meta:
        model = Intern
        fields = ['name','program','location','phone']
        labels = {'name':"Enter Name",'phone':'Mobile Number'}
        help_text = {'name': 'full name'}
        error_messages = {
            'name':{ 'required' : "Intern Full name is required"},
            'program':{'required':'Program should be given', 'max_length': 'length should not be greater than 50'}
            }
        
        widgets = {
            'program' : forms.TextInput(
                attrs = {
                    'class' : 'my-class',
                    'placeholder' : 'Django...'
                }
            )
        }

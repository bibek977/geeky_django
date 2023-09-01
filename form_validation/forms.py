from typing import Any, Dict
from django import forms
from django.core import validators

class StudentForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    semail = forms.CharField()

    # for one field

    # def clean_sname(self):
    #     sname = self.cleaned_data["sname"]
    #     if len(sname) < 5:
    #         raise forms.ValidationError("User name is too short")
    #     return sname

    # for many fields
    # this required validation in html but why?

    def clean(self):
        cleaned_data = super().clean()

        id = self.cleaned_data['sid']
        if id == 161743:
            raise forms.ValidationError("This is reserved")
        
        email = self.cleaned_data['semail']
        if len(email) < 5:
            raise forms.ValidationError("Too short email")
        



def my_name(value):
    if str(value).lower() == "bibek":
        raise forms.ValidationError("This name is reserverd")
    
class StudentTwoForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField(validators=[my_name])
    semail = forms.CharField(validators=[validators.MaxLengthValidator(5)])

    sroll = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()

        sid = self.cleaned_data['sid']
        sroll = self.cleaned_data['sroll']

        if sid == sroll:
            raise forms.ValidationError("id and roll no are  same")
        

class StudentThreeForm(forms.Form):

    error_css_class = 'error_css'
    required_css_class = 'required_css'

    sid = forms.IntegerField(error_messages={"required" : "Student Id is required"})
    sname = forms.CharField(max_length=100, min_length=5, error_messages={'required':'student name is always required', 'min_length':'student name should be greater than 5 letters'})
    semail = forms.EmailField(min_length=5,error_messages={"required" : "Email of student must be given", 'min_length':'student name should be greater than 5 letters'})
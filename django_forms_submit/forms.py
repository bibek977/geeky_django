from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(min_length=5,max_length=50,strip=False,error_messages={'required':'Enter your name'})
    roll = forms.IntegerField(min_value=5,max_value=100)
    # roll = forms.IntegerField(required=False)
    program = forms.CharField(empty_value="python")
    agree = forms.BooleanField(label_suffix='',label="I Agree")
    gpa = forms.DecimalField(max_value=100,max_digits=4,decimal_places=1)
    percent = forms.FloatField(max_value=50,min_value=2)
    about = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
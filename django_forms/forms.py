from django import forms

class StudentForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    semail = forms.CharField()
    spass = forms.CharField(help_text="This is a sample text")

    colz_name = forms.CharField(initial="Ncit")

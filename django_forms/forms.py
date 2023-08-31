from django import forms

class StudentForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    semail = forms.CharField()
    spass = forms.CharField(help_text="This is a sample text")

    colz_name = forms.CharField(initial="Ncit")


class StudentTwoForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    semail = forms.CharField()
    spass = forms.CharField(widget=forms.HiddenInput())

    # spass = forms.CharField(widget=forms.PasswordInput())
    # spass = forms.CharField(widget=forms.EmailInput())
    # spass = forms.CharField(widget=forms.URLInput())
    # spass = forms.CharField(widget=forms.DateInput())
    # spass = forms.CharField(widget=forms.DateTimeInput())
    # spass = forms.CharField(widget=forms.TimeInput())
    # spass = forms.CharField(widget=forms.Textarea())
    # spass = forms.CharField(widget=forms.CheckboxInput())
    # spass = forms.CharField(widget=forms.Select())
    # spass = forms.CharField(widget=forms.SelectMultiple())
    # spass = forms.CharField(widget=forms.NullBooleanField())
    # spass = forms.CharField(widget=forms.RadioSelect())
    # spass = forms.CharField(widget=forms.CheckboxSelectMultiple())
    # spass = forms.CharField(widget=forms.FileInput())
    # spass = forms.CharField(widget=forms.ClearableFileInput())
    # spass = forms.CharField(widget=forms.MultipleHiddenInput())
    # spass = forms.CharField(widget=forms.SplitDateTimeWidget())


class StudentThreeForm(forms.Form):
    sid = forms.IntegerField(label="student id",label_suffix=" ",initial="43",required=False,disabled=True,help_text="This is college id")
    sname = forms.CharField()
    semail = forms.CharField()


    # other tags needs to learn are
    # error_messages
    # validators
    # localize


class StudentFourForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    semail = forms.EmailField()
    # spass = forms.CharField(widget=forms.PasswordInput())
    spass = forms.CharField(widget=forms.PasswordInput)
    sabout = forms.CharField(widget=forms.Textarea)
    sgrade = forms.CharField(widget=forms.CheckboxInput)

    sdesc = forms.CharField(widget=forms.TextInput(attrs={'class' : 'desc description' , 'id' : 'descId'}))
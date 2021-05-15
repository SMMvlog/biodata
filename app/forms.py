from django import forms
from .models import Resume

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female")
)

JOB_CHOICES = (
    ("Mumbai", "Mumbai"),
    ("Delhi", "Delhi"),
    ("Noida", "Noida"),
    ("Gurgaon","Gurgaon"),
    ("Pune", "Pune"),
    ("Bangalore", "Bangalore")
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={'id':'gender'}))
    job_city = forms.MultipleChoiceField(label='Preferred job location', choices=JOB_CHOICES,widget=forms.CheckboxSelectMultiple(attrs={'id':'job_city'}))
    class Meta:
        model = Resume
        fields = "__all__"

        labels = {'name':'Full Name','dob':'Date of Birth','pin':'pin code','mpbile':'Mobile No','email':'Email ID'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
                   'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
                    'locality':forms.TextInput(attrs={'class':'form-control','id':'locality'}),
                    'city':forms.TextInput(attrs={'class':'form-control','id':'city'}),
                    'pin':forms.NumberInput(attrs={'class':'form-control','id':'pin'}),
                    'state':forms.Select(attrs={'class':'form-select','id':'state'}),
                    'mobile':forms.NumberInput(attrs={'class':'form-control','id':'mobile'}),
                    'email':forms.EmailInput(attrs={'class':'form-control','id':'email'})}



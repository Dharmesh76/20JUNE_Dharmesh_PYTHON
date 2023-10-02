from django import forms
from .models import *

class signUPform(forms.ModelForm):
    class Meta:
        model=studentModel
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=studentModel
        fields=['first_name','last_name','dob','email','phone','address',]        
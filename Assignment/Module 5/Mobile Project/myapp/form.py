from django import forms
from .models import *


class adddataform(forms.ModelForm):
    class Meta:
        model=product_sub_category_details
        fields='__all__'
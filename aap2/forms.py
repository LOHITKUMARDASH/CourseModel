from django import forms
from aap2.models import  CourseModel
import re

class CourseForm(forms.ModelForm):
    fee=forms.FloatField(min_value=0)
    class Meta:
        model=CourseModel
        fields="__all__"

    def clean_name(self):
        name=self.cleaned_data['name']
        res=re.findall(r'^[A-Z a-z]*$',name)
        if res:
            return name
        else:
            raise forms.ValidationError('Name only accept characters,A-Z and a-z')
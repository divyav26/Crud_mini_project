from django import forms
from .models import User


class Student(forms.ModelForm):
    class Meta:
        model = User
        fields =['name', 'uclass','div','rollno','email','contact']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'uclass': forms.TextInput(attrs={'class': 'form-control'}),
            'div': forms.TextInput(attrs={'class': 'form-control'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),

        }
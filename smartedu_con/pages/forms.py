from dataclasses import fields
from django import forms
from.models import Contact

class ContactForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}))
    message=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'message'}))
    class Meta:
        model=Contact
        fields=('first_name','last_name','phone','message','email')
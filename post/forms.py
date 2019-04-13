from django.forms import ModelForm, forms
from post.models import Party
from django import forms
from django.forms import ModelForm


class PartyForm(ModelForm):
     class Meta:
         model = Party
         fields = ['city', 'title', 'description', 'image','location','date']

         widgets = {
             'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
             'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
             'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
         }
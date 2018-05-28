from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    country = forms.CharField(max_length=400)
    capital = forms.CharField(max_length=400)
    language = forms.CharField(max_length=400)
    habitants = forms.CharField(max_length=400)
    continent = forms.CharField(max_length=255)
    square_kilometers = forms.CharField(max_length=255)
    
    class Meta:
        model = Country
        fields = ('country', 'capital', 'language', 'habitants', 'continent', 'square_kilometers')



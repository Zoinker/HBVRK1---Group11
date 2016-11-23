from django.contrib.auth.models import User
from django import forms
from driver.models import Driver


class SearchForm(forms.ModelForm):
    zoneFrom = forms.CharField()
    zoneTo = forms.CharField()

    class Meta:
        model = Driver
        fields = ['zoneFrom', 'zoneTo']
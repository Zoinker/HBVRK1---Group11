from django.contrib.auth.models import User
from django import forms
from driver.models import Driver, Zone

LOCATIONS = (
    ('Breiðholt', 'Breiðholt'),
    ('Washington', 'Washington'),
    ('Moskva', 'Moskva'),
    ('Garðabær', 'Garðabær'),
)

class SarchForm(forms.ModelForm):
    zoneFrom = forms.CharField()
    zoneTo = forms.CharField()

    class Meta:
        model = Driver
        fields = ['zoneFrom', 'zoneTo']

class SearchForm(forms.ModelForm):
    zoneFrom = forms.ChoiceField(choices=LOCATIONS, required=True )
    zoneTo = forms.ChoiceField(choices=LOCATIONS, required=True )

    class Meta:
        model = Driver
        fields = ['zoneFrom', 'zoneTo']


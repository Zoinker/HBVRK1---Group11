from django.contrib.auth.models import User
from django import forms
from driver.models import Driver, Zone
LOCATIONS = (
    ('Breiðholt', 'Breiðholt'),
    ('Washington', 'Washington'),
    ('Moskva', 'Moskva'),
    ('Garðabær', 'Garðabær'),
    ('Hafnafjörður', 'Hafnafjörður'),
    ('Kópavogur', 'Kópavogur'),
    ('Mosfellsbær', 'Mosfellsbær'),
    ('Seltjarnarnes', 'Seltjarnarnes'),
    ('Miðbær', 'Miðbær')
)

class setZonesForm(forms.ModelForm):
    zones = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LOCATIONS)

    class Meta:
        model = Driver
        fields = ['zones']




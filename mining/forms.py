from django import forms
from django.core.validators import RegexValidator


# my_validator = RegexValidator(regex=r'/^[0-9]{1,}\s[0-9]{1,}$/', message='input like X Y')

class Input(forms.Form):
    coordinate = forms.CharField(max_length=10,required=False)#, validators=[my_validator])


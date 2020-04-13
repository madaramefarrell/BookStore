from django import forms
from django.forms import widgets

from .models import Order


class OrderCreateForm(forms.ModelForm):
    name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    email = forms.EmailField(required=True,
                             widget=widgets.TextInput(
                                 attrs={'placeholder': 'Input your email and I\'ll send you a mail'}))
    postal_code = forms.CharField(required=True)
    city = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = ['name', 'address', 'email',
                  'postal_code', 'city', ]

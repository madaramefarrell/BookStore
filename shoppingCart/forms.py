from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Cart
from catalog.models import Book


class CartAddForm(forms.ModelForm):
    number = forms.IntegerField(min_value=0, required=False,
                                widget=widgets.NumberInput(attrs={
                                    'class': 'span1',
                                    'value size': '16',
                                    'style': 'max-width:34px',
                                }))
    class Meta:
        model = Cart
        fields = ('number',)

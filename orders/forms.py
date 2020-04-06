from django import forms

from .models import Order
from account.models import CustomerUser


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address',
                  'postal_code', 'city']

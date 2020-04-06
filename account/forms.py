from django import forms
from django.forms import widgets
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import CustomerUser, VendorUser
from django.utils.translation import gettext_lazy as _
from django.core.mail import EmailMessage


class MyUserCreationForm(UserCreationForm):
    account = forms.CharField(max_length=30, required=True, widget=widgets.TextInput(attrs={}))
    email = forms.EmailField(required=True, widget=widgets.TextInput(attrs={}))
    name = forms.CharField(max_length=30, widget=widgets.TextInput(attrs={}))

    # To create a unique email field in your Django User model
    # User._meta.get_field('email').unique = True

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('account', 'name', 'password1', 'password2', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.username = self.cleaned_data['account']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user


class CustomerUserForm(forms.ModelForm):
    secondary_email = forms.EmailField(required=False, widget=widgets.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomerUser
        fields = ('secondary_email',)


class VendorUserForm(forms.ModelForm):
    secondary_email = forms.EmailField(required=False, widget=widgets.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = VendorUser
        fields = ('secondary_email',)


class LoginForm(forms.Form):
    account = forms.CharField(required=True, widget=widgets.TextInput(attrs={'class': 'aaac'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ('account', 'password',)


class ChangePersonalInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=30, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=widgets.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = {'name', 'email', }


class forgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=widgets.TextInput(attrs={'class': 'span4', 'placeholder': 'Your email'}))

    class Meta:
        fields = {'email', }



"""  Use this Django form create function
class RestPasswordForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = {'email', 'new_password', }
class RestPasswordForm(RestPasswordForm):
    pass
class PasswordChangeForm(PasswordChangeForm):
    pass
"""

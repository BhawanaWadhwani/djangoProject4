from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, label="User Name")
    email = forms.EmailField(required=True, label="Email ID")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Password")
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True, label="Confirm Password")
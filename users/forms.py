from django import forms

class RegisterUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
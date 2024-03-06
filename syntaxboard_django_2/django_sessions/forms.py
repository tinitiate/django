from django import forms

class LoginForm(forms.Form):
    # HTML INPUT Box
    userid = forms.CharField()
    passwd = forms.CharField(max_length=32, widget=forms.PasswordInput)

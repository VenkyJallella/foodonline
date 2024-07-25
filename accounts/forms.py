from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['firstName','lastName','email','username','password']

    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')

        if password != confirmPassword:
            raise forms.ValidationError('password does not match')

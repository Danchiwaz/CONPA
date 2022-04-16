from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ClearableFileInput

class UserRegisteForm(UserCreationForm):
    email = forms.EmailField(required= True)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = "__all__"
        exclude = ['user', 'attached','disqualify','Qualified']
        # widgets = {
        #     'file': ClearableFileInput(attrs={'multiple': True}),
        # }
    
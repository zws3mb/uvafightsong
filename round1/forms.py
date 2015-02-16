from django import forms
#from models import Bulletin,Document,Folder,Permission
from models import Submission
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
class AccountForm(forms.Form):
    username=forms.CharField(
        label='Computing ID'
    )
    password=forms.CharField(label='Password',widget=forms.PasswordInput())
    email=forms.CharField(label='Email',widget=forms.EmailInput())

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username= forms.CharField(label='Computing ID')
    #Type = forms.ChoiceField(choices=('Author','Reader'))
    #nested Meta class
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')

class SubmissionForm(forms.ModelForm):
    mp3 = forms.FileField(label='Select an mp3 file')
    lyrics = forms.FileField(label='Select a lyrics file')
    author1=forms.CharField(label='Author 1')
    author2=forms.CharField(label='Author 2',required=False)
    author3=forms.CharField(label='Author 3',required=False)
    class Meta:
        model=Submission
        fields = ('title','text_description','mp3','lyrics','author1','author2','author3')
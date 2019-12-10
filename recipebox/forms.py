from django.forms import ModelForm, Form 
from recipebox.models import Author, Recipe
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class AuthorForm(Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)

class RecipeForm(ModelForm):
    class Meta():
        model = Recipe
        fields = ['title', 'author', 'description', 'time_required', 'instructions']
        
class SignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
   password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class SignUpForm(Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1']
        )
        return user


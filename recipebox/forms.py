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

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


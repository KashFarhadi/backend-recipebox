from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from recipebox.models import Recipe, Author
from .forms import AuthorForm, RecipeForm, SignInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'index.html', {'recipe_list': recipe_list})

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    author = Author.objects.get(name=recipe.author)
    print(author)
    return render(request, 'recipe.html', {'recipe': recipe, 'author': author})

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    authors_recipes = author.recipe_set.all()
    return render(request, 'author.html', {'author': author, 'authors_recipes': authors_recipes})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = RecipeForm()
    return render(request, 'form.html', {'form': form})

@staff_member_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = AuthorForm()
    return render(request, 'form.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    else:
        if request.method == 'POST':
            form = SignInForm(data=request.POST)
            if form.is_valid():
                    login(request, form.get_user())
                    return HttpResponseRedirect('/')

        else:
            form = SignInForm()
    return render(request, 'form.html', {'form': form})

# @staff_member_required
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


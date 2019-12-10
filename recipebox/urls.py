"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox.views import index, recipe, author, add_author, add_recipe, login_view, logout_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('<int:recipe_id>/', recipe , name='recipe'), 
    path('author/<int:author_id>/', author, name='author'),
    path('addauthor/', add_author, name='add_author'),
    path('addrecipe/', add_recipe, name='add_recipe'),
    path('login/', login_view),
    path('logout/', logout_view, name='logout_view'),
    path('signup/', signup_view, name='signup'),

]

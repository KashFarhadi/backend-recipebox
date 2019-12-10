# Welcome to Django! Recipebox
Django is the most popular Python web framework for making user-facing applications. This is an a new application using DJango that serves recipes from different authors.


## Creator
Kash Farhadi

## Complete Instructions for Running the Application

Fork and clone the project and navigate to that directory

Create and start a a virtual environment

for virtualenv:
`virtualenv env --no-site-packages

source env/bin/activate`

for pipenv:
`pipenv -install
pipenv shell`


python manage.py migrate

Create a admin account if you would like to test admin features and access the admin page

`python manage.py createsuperuser`


Run `python manage.py makemigrations {foldername}` 
(where foldername is the top level folder for this project)

Run `python manage.py migrate` to push  to the db

Start the django server using 

`python manage.py runserver`

You can then access the homepage of the app the following web addresses
`http://127.0.0.1:8000/` 
`http://localhost:8000/`

The django admin page can be accessed at the `/admin/` extension

You can login as a user at 
`http://localhost:8000/login/`
`http://127.0.0.1:8000/login/`



### Built using Python 3.8 and the latest version of Django (2.1.2 as of this writing)

## Existing Users 

Admin user 
username: kash
password: optix

Regular user 
username: testing 
password: djangoform

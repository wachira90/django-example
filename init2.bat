@ECHO ON
pip install django
pip install djangorestframework
django-admin startproject appmain
CD appmain
python manage.py startapp api
python manage.py runserver 0.0.0.0:8000

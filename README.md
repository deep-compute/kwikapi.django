# Use kwikapi in Django

## Install kwikapi for Django
```bash
$ pip install kwikapi[django]
```

## Create a Django project (Ref: https://docs.djangoproject.com/en/1.9/intro/tutorial01/)
```bash
$ django-admin startproject django_kwikapi
```

## Create an app in Django
```bash
$ python manage.py startapp polls
``

#### Add your app name to settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
]
```
## /django_kwikapi/django_kwikapi/urls.py
```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('polls.urls'))
]
```

## /django_kwikapi/polls/urls.py
```python
from django.conf.urls import url, include

from . import views
from kwikapi.django import RequestHandler

urlpatterns = [
    url(r'api/', RequestHandler(views.api).handle_request),
]
```

## /django_kwikapi/polls/views.py
```python
from django.http import HttpResponse
from kwikapi import API
from logging import Logger

class BaseCalc():
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

class StandardCalc():
    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> int:
        return a / b

api = API(Logger, default_version='v1')
api.register(BaseCalc(), 'v1')
api.register(StandardCalc(), "v2")
```

## Start Django
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 8888
```

## Make API request
```bash
$ curl http://localhost:8888/api/v1/add?a=10&b=10
$ curl http://localhost:8888/api/v2/divide?a=10&b=10
```

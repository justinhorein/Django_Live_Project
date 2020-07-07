from django.urls import include, path
from . import views

from django.contrib import admin
from django.urls import include, path

## URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
## Third is the name of the pattern/function.

urlpatterns = [
    path('', views.index, name='home'),
]

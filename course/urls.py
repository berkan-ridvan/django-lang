from django.urls import path
from course.views import index
from django.db import models
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

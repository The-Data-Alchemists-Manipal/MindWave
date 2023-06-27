from django import forms
from django import views
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('diabetes/',views.diabetes,name='diabetes'),
    path('result_diabetes/',views.result_diabetes,name='result_diabetes'),
]
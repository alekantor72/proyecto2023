'''
from django.urls import path, include
from . import views

app_name='usuarios'

urlspatterns = [
	path('Registro', views.Registro, name="registrar"),
	
]
'''
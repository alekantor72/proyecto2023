
from django.urls import path, include
from . import views

app_name='comentarios'

urlpatterns = [
	
	path('Agregar/<int:pk>', views.Agregar, name='agregar_comentarios'),
	
]
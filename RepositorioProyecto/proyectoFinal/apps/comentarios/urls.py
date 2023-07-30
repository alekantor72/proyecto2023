
from django.urls import path, include
from . import views

app_name='comentarios'

urlpatterns = [
	
	path('Agregar/<int:pk>', views.Agregar, name='agregar_comentarios'),
	path('Borrar/<int:pk>', views.BorrarComentario.as_view(), name="borrar_comentario"),
	path('Modificar/<int:pk>', views.ModificarComentario.as_view(), name="modificar_comentario"),
	
]
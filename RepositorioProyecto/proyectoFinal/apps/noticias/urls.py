
from django.urls import path, include
from . import views

app_name='noticias'

urlpatterns = [
	path('Crear', views.CrearNoticia.as_view(), name="crear_noticia"),

	path('Listar', views.ListarNoticias.as_view(), name="listar_noticias"),

	path('Detalle/<int:pk>', views.DetalleNoticiaF, name="detalle_noticias"),

	path('Categorias/', views.Categorias.as_view(), name="categorias"),	

	path('Filtro/<int:pk>', views.Filtro_Categoria, name="filtro_categoria"),

	path('Borrar/<int:pk>', views.BorrarNoticia.as_view(), name="borrar_noticia"),

	path('Modificar/<int:pk>', views.ModificarNoticia.as_view(), name="modificar_noticia"),

]

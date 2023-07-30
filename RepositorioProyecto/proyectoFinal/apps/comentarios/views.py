from django.shortcuts import render, HttpResponseRedirect
from apps.noticias.models import Noticia
from apps.comentarios.models import Comentario

from django.urls import	reverse_lazy

def Agregar(request, pk):
	com = request.POST.get('comentario', None)
	usuario = request.user
	noticia = Noticia.objects.get(id = pk)

	Comentario.objects.create(texto = com, usuario = usuario, noticia = noticia)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticias' , kwargs={'pk':pk}))
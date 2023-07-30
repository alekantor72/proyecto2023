from django.shortcuts import render, HttpResponseRedirect
from apps.noticias.models import Noticia
from apps.comentarios.models import Comentario
from django.views.generic import DeleteView, UpdateView
from django.urls import	reverse_lazy

from .forms import Form_Modificacion


def Agregar(request, pk):
	com = request.POST.get('comentario', None)
	usuario = request.user
	noticia = Noticia.objects.get(id = pk)

	Comentario.objects.create(texto = com, usuario = usuario, noticia = noticia)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticias' , kwargs={'pk':pk}))


class BorrarComentario(DeleteView):
	model = Comentario
	success_url = reverse_lazy('noticias:listar_noticias')

class ModificarComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'comentarios/modificar.html'
	success_url = reverse_lazy('noticias:listar_noticias') 

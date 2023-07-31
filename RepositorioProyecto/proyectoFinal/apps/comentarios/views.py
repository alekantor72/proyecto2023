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
	def get_success_url(self):
		return reverse_lazy('noticias:detalle_noticias',kwargs={'pk': self.object.noticia.pk})
	

class ModificarComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'comentarios/modificar.html'
	def get_success_url(self):
		return reverse_lazy('noticias:detalle_noticias',kwargs={'pk': self.object.noticia.pk})
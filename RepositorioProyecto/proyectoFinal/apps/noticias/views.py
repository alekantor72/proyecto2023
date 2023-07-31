from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Noticia, Categoria
from .forms import Form_Alta, Form_Modificacion

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.mixins		import UserPassesTestMixin

class CrearNoticia(LoginRequiredMixin,UserPassesTestMixin, CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/crear.html'
	success_url = reverse_lazy('noticias:listar_noticias') 


	def test_func(self):
		return self.request.user.is_staff

	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)



class ListarNoticias(ListView):
	model = Noticia
	template_name = 'noticias/listar.html'
	#POR DEFECTO ESTA VISTA MANDA AL TEMPLATE UNA VARIABLE
	#LLAMADA OBJECT_LIST, CON LA LISTA DE TODAS LAS NOTICIAS		



def DetalleNoticiaF(request, pk):
	ctx = {}
	noti = Noticia.objects.get(id = pk)
	ctx['noticia'] = noti
	return render(request, 'noticias/detalle.html', ctx)



class Categorias(ListView):
	model = Categoria
	template_name = 'noticias/categorias.html'

def Filtro_Categoria(request, pk):
	ctx = {}
	cate = Categoria.objects.get(id = pk)
	filtradas = Noticia.objects.filter(categoria = cate)
	ctx['object_list'] = filtradas
	return render(request, 'noticias/listar.html', ctx)

class BorrarNoticia(DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:listar_noticias')

class ModificarNoticia(UpdateView):
	model = Noticia
	form_class = Form_Modificacion
	template_name = 'noticias/Modificar.html'
	success_url = reverse_lazy('noticias:listar_noticias') 
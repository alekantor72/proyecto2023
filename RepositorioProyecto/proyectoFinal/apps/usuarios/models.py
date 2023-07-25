from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
	creado = models.DateTimeField(
		'creado',
		auto_now_add=True
	)
	modificado = models.DateTimeField(
		'modificado'
		auto_now_add)



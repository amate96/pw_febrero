from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Partido_politico(models.Model):
	nombre = models.CharField(max_length=120, unique=True)

class Circunscripcion(models.Model):
	nombre = models.CharField(max_length=120)
	num_esca = models.IntegerField()

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("sistema:circun_detail", kwargs={"pk": self.pk})

	def get_absolute_url_delete(self):
		return reverse("sistema:circun_delete", kwargs={"pk": self.pk})

	def get_absolute_url_update(self):
		return reverse("sistema:circun_update", kwargs={"pk": self.pk})


class Mesa(models.Model):
	nombre = models.CharField(max_length=120)
	circunscripcion = models.ForeignKey('Circunscripcion')

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("sistema:mesa_detail", kwargs={"id": self.id})

	def get_absolute_url_update(self):
		return reverse("sistema:mesa_update", kwargs={"id": self.id})


class Resultado(models.Model):
	votos = models.IntegerField(default=0)
	partido = models.ForeignKey('Partido_politico')
	mesa = models.ForeignKey('Mesa')
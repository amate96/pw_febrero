from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.FileField(null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
		
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["-timestamp", "-updated"]

	def get_absolute_url_edit(self):
		return reverse("posts:update", kwargs={"id": self.id})

	def get_absolute_url_delete(self):
		return reverse("posts:delete", kwargs={"id": self.id})

class Commentary(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=2)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	post = models.ForeignKey('Post')



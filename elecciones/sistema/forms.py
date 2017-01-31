
from django import forms

from .models import Mesa
from django.contrib.auth.models import User


class MesaForm(forms.ModelForm):
	class Meta:
		model = Mesa
		fields = ["nombre", "circunscripcion"]

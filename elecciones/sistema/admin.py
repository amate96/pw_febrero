from django.contrib import admin

# Register your models here.

from .models import Partido_politico, Circunscripcion, Mesa, Resultado

admin.site.register(Partido_politico)
admin.site.register(Circunscripcion)
admin.site.register(Mesa)
admin.site.register(Resultado)
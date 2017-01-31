from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.contrib import messages

# Create your views here.

from .models import Partido_politico, Circunscripcion, Mesa, Resultado

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from .forms import MesaForm


def inicio(request):
	context = {
		}
	return render(request, "inicio.html", context)

#Test para comprobar supervisor
def is_supervisor(user):
    return user.is_superuser

class CircunList(ListView):
    model = Circunscripcion
    template_name = "sistema/circun_list.html"

class CircunDetail(DetailView):
	model = Circunscripcion
	template_name = "sistema/circun_detail.html"

class CircunCreate(CreateView):
	model = Circunscripcion
	template_name = "sistema/circun_create.html"
	fields = ['nombre','num_esca']

	@method_decorator(user_passes_test(is_supervisor))
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(CircunCreate, self).dispatch(request, *args, **kwargs)

class CircunDelete(DeleteView):
	model = Circunscripcion
	template_name = "sistema/circun_delete.html"
	success_url = reverse_lazy('sistema:circun_list')

	@method_decorator(user_passes_test(is_supervisor))
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(CircunCreate, self).dispatch(request, *args, **kwargs)

class CircunUpdate(UpdateView):
	model = Circunscripcion
	template_name = "sistema/circun_update.html"
	fields = ['nombre','num_esca']

	@method_decorator(user_passes_test(is_supervisor))
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(CircunCreate, self).dispatch(request, *args, **kwargs)


def mesa_list(request, id=None):
	if Circunscripcion.objects.filter(id=id).exists():
		circunscripcion = Circunscripcion.objects.get(id=id)
		mesas = circunscripcion.mesa_set.all()
		context = {
			"circunscripcion_tit": circunscripcion.nombre,
			"mesas": mesas

		}
		return render(request, "mesas_list.html", context)
    
	else:
		return redirect('/notfound')

def mesa_detail(request, id=None):
	instance = get_object_or_404(Mesa, id=id)
	
	
	context = {
		"instance": instance

		}
	return render(request, "mesa_detail.html", context)


def mesa_detail(request, id=None):
	instance = get_object_or_404(Mesa, id=id)
	
	
	context = {
		"instance": instance

		}
	return render(request, "mesa_detail.html", context)

@login_required
@user_passes_test(is_supervisor)
def mesa_create(request):
	if not (request.user.is_superuser):
		raise Http404

	form = MesaForm(request.POST or None)
	if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "mesa_form.html", context)

@login_required
@user_passes_test(is_supervisor)
def mesa_update(request, id=None):
	if not (request.user.is_superuser):
		raise Http404

	instance = get_object_or_404(Mesa, id=id)
	form = MesaForm(request.POST or None, instance=instance)
	if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "mesa_form.html", context)
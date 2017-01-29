from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.contrib import messages

# Create your views here.
from .models import Post, Commentary
from .forms import PostForm, CommentaryForm, UserForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth import login
from django.contrib.auth.models import User

from django.views import View




def post_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request, "Successfully created")
			return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	try:
		commentary_list = Commentary.objects.filter(post=instance)
	except:
		commentary_list = None
	
	form = CommentaryForm(request.POST or None)
	if form.is_valid():
			instance2 = form.save(commit=False)
			try:
				instance2.user = request.user
			except:
				pass

			instance2.post = instance
			instance2.save()
			messages.success(request, "Successfully created a commentary")
			return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": instance.title,
			"instance": instance,
			"form":form,
			"commentary_list":commentary_list

		}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|Q(content__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 5) # Show 5 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
			"object_list": queryset,
			"title": "List"
		}
	return render(request, "post_list.html", context)
	
class post_update(View):
	model = Post
	def get(self, request, id=None):
		if not (request.user.is_staff or request.user.is_superuser):
			raise Http404
		instance = get_object_or_404(Post, id=id)
		form = PostForm(request.POST or None,  request.FILES or None, instance=instance)
		context = {
			"title": instance.title,
			"instance": instance,
			"form": form,
		}
		return render(request, "post_form.html", context)

	def post(self, request, id=None):
		if not (request.user.is_staff or request.user.is_superuser):
			raise Http404
		instance = get_object_or_404(Post, id=id)
		form = PostForm(request.POST or None,  request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Saved")
			return HttpResponseRedirect(instance.get_absolute_url())
		
		
def post_delete(request, id=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Succesfully deleted")
	return redirect("posts:list")

def adduser(request):
	form = UserForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		new_user = User.objects.create_user(**form.cleaned_data)
		login(request, new_user)
		messages.success(request, "Succesfully created new user")
		return redirect("posts:list")

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
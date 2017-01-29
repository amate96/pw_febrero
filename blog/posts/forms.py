from django import forms

from .models import Post, Commentary
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content", "image"]

class CommentaryForm(forms.ModelForm):
	class Meta:
		model = Commentary
		fields = ["content"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
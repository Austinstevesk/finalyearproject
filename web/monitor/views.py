from django.shortcuts import render, get_object_or_404
'''Returns object or 404 error
if the object does not exist'''
from django.http import HttpResponse
#Mixins works as login required but with class based views
#Our PostCreateView is class based so we have to use it
#Note the prular while importing but singular while using it 
#UserPassesTestMixin ensures that only the author of a post can update it
#It needs a function created which runs to test if the user is the author
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Post
from django.contrib.auth.models import User


# Create your views here.



'''def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blogapp/home.html', context)'''

#works as the new homepage 

#Details for the post
def home(request):
	return render(request, 'monitor/home.html')

class PostDetailView(DetailView):
	model = Post

#Creating a post
#Mixins should be at the left
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		"""setting the author of a post to the current logged in author before
		submitting the form so as the post can have an author before being created"""
		form.instance.author = self.request.user
		return super().form_valid(form)

		
def about(request):
	return render(request, 'monitor/about.html', {'title': "Austin's Gas Monitoring"})

def contact(request):
	return render(request, 'monitor/contact.html')

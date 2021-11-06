from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.

def home(request):
	context = {
		'posts' : Post.objects.all(),
		'title' : 'Blogs by Yukty'
	}
	return render(request,'blog/home.html',context)

class PostListView(ListView) :
	model = Post
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 4

class PostDetailView(DetailView):
	model = Post

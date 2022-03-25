from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.
class BlogViewsList(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context ={
            'posts' : posts
        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *arg, **kwarg):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)
    def post(self, request, *arg, **kwarg):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")

                p, create = Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect('blog:home')

        context = {

        }
        return render(request, 'blog_create.html', context)

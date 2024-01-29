from django.shortcuts import render,redirect
from.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from.forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib.auth import logout

# Create your views here.

# def home(request):
#     return render(request,'index.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'index1.html'
    ordering = ['-id']
    # ordering = ['post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post1.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def userlogout(request):
    logout(request)
    return redirect('/')

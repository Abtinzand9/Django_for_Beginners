from django.shortcuts import render
from django.views.generic import ListView , CreateView , DetailView , DeleteView , UpdateView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name='article/update.html'
    fields = (
        'title',
        'body',
    )
    
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("article_list")
    template_name = 'article/delete.html'

class ArticleCreateView(CreateView):
    model = Article
    fields = (
        'title',
        'body',
        'author'
    )
    template_name = 'article/create.html'
from django.shortcuts import render
from django.views.generic import ListView , CreateView , DetailView , DeleteView , UpdateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.
class ArticleListView(LoginRequiredMixin ,ListView):
    model = Article
    template_name = 'article/list.html'


class ArticleDetailView(LoginRequiredMixin ,DetailView):
    model = Article
    template_name = 'article/detail.html'


class ArticleUpdateView(LoginRequiredMixin ,UserPassesTestMixin,UpdateView):
    model = Article
    template_name='article/update.html'
    fields = (
        'title',
        'body',
    )
    def test_func(self) :
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDeleteView(LoginRequiredMixin ,UserPassesTestMixin ,DeleteView):
    model = Article
    success_url = reverse_lazy("article_list")
    template_name = 'article/delete.html'
    def test_func(self) :
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin ,CreateView):
    model = Article
    fields = (
        'title',
        'body',
    )
    template_name = 'article/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView  , DetailView , FormView
from django.views.generic.edit import DeleteView , UpdateView , CreateView 
from django.views.generic.detail import SingleObjectMixin
from .models import Article ,Comment
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .forms import CommentForm
from django.views import View

# Create your views here.
class ArticleListView(LoginRequiredMixin ,ListView):
    model = Article
    template_name = 'article/list.html'

class CommentGet(DetailView):
    model = Article
    template_name = 'article/detail.html'

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin , FormView):
    model = Article
    form_class = CommentForm
    template_name='article/detail.html'

    def post(self, request, *args, **kwargs) :
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self) :
        article = self.get_object()
        return reverse("article_detail" , kwargs={'pk':article.pk})
    

class ArticleDetailView(LoginRequiredMixin ,View):
    def get(self ,request ,*args, **kwargs):
        View =CommentGet.as_view()
        return View(request , *args, **kwargs)
    
    def post(self ,request ,*args, **kwargs):
        View =CommentPost.as_view()
        return View(request , *args, **kwargs)

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
    
from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from .models import Article

# Create your views here.
def home(request):
    return render(request, 'Category/home.html')

class ArticleListView(ListView):
    model = Article
    template_name = 'Category/articles/articles.html'
    # login_url = 'accounts/login/'

class ArticleDetailView (DetailView):
    model = Article
    template_name = 'Category/articles/articles-details.html'
    # login_url = 'accounts/login/'
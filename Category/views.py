from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Category/home.html'


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'Category/articles/articles.html'
    login_url = 'accounts/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        category = self.request.GET.get('category', 'all')

        if query:
            queryset = queryset.filter(name__icontains=query)
        if category and category!= 'all':
            queryset = queryset.filter(category__name__iexact=category)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get('category', 'all')
        return context

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'Category/articles/articles-details.html'
    login_url = 'accounts/login/'


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ['category', 'type', 'name', 'born', 'died', 'nationality', 'known_for', 'notable_work', 'about', 'year', 'medium', 'dimensions', 'location', 'designed_by', 'developer']
    template_name = 'Category/articles/articles-create.html'
    success_url = reverse_lazy('articles')

    def test_func(self):
        return self.request.user.groups.filter(name='Tutors').exists() or self.request.user.groups.filter(name='Administrators').exists()


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['category', 'type', 'name', 'born', 'died', 'nationality', 'known_for', 'notable_work', 'about', 'year', 'medium', 'dimensions', 'location', 'designed_by', 'developer']
    template_name = 'Category/articles/articles-update.html'
    success_url = reverse_lazy('articles')

    def test_func(self):
        return self.request.user.groups.filter(name='Tutors').exists() or self.request.user.groups.filter(name='Administrators').exists()


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'Category/articles/articles-delete.html'
    success_url = '/articles/'

    def test_func(self):
        return self.request.user.groups.filter(name='Administrators').exists()


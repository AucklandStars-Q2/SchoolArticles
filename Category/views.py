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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        category = self.request.GET.get('category', 'all')

        if query:
            queryset = queryset.filter(name__icontains=query)
        if category and category != 'all':
            queryset = queryset.filter(category__name__iexact=category)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get('category', 'all')
        return context

class ArticleDetailView (DetailView):
    model = Article
    template_name = 'Category/articles/articles-details.html'
    # login_url = 'accounts/login/'
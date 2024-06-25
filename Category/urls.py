from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/create/', views.ArticleCreateView.as_view(), name='articles-create'),
    path('articles/<pk>/', views.ArticleDetailView.as_view(), name='articles-details'),
    path('articles/<pk>/update/', views.ArticleUpdateView.as_view(), name='articles-update'),
    path('articles/<pk>/delete/', views.ArticleDeleteView.as_view(), name='articles-delete'),
    path('articles/accounts/', include('django.contrib.auth.urls')),
]
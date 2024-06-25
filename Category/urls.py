from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='articles-details'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('articles', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='articles-details'),
]
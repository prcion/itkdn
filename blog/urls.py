from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowNewsList.as_view(), name='blog-home'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('test/', views.contacts, name='blog-test'),
]

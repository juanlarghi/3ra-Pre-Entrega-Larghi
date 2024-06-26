from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/search/', views.blog_search, name='blog_search'),
    path('blog/fullview/<int:pk>', views.blog_fullview, name='blog_fullview'),
    path('blog/update/<int:pk>', views.blog_update, name='blog_update'),
    path('blog/delete/<int:pk>', views.blog_delete, name='blog_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_home, name='blog-home-page'),
    path('posts',views.show_all_post, name='all-posts-page'),
    path('posts/<slug:slug>',views.post_detail, name='post-detail-page')
]
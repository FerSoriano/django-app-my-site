from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('posts',views.show_all_post, name='all_posts'),
    path('post/<int:id>',views.show_post_by_id, name='post')
]
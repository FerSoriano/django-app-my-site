from django.shortcuts import render
from django.http import HttpResponse

posts = {
    1: "This is my first post",
    2: "Idk if this is the best way to do that",
    3: "Let's finish with the third one"
}

def blog_home(request):
    return render(request, 'blog/home.html')

def show_all_post(request):
    return render(request, 'blog/posts.html',{
        'posts' : posts
    })

def post_detail(request, id):
    post = posts[id]
    return render(request, 'blog/post.html',{
        "id": id,
        "post" : post
    })
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-post_timestamp')[:5]
    blogs = Blog.objects.order_by('-post_timestamp')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})  

def blog_detail(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})    # dict with id is passed to the detail.html Template


# def social_media_links(request):
#     return render(request, 'blog/social_media.html')

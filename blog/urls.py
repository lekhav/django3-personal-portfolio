from django.urls import path
from . import views

app_name = 'blog'        # setting the app_name, to be used in Template's
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),     # Go to views.py inside the app and make function all_blogs
    path('<int:blog_id>/', views.blog_detail, name='detail'), 

    # any int after /blog/ in URL passes the blog_id to the view.py -> post_detail function
    # path('<str:blog_id>/', views.blog_detail, name='detail'),
    # path('social', views.social_media_links, name="social_media_links"),
]

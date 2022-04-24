from django.urls import path

from adventure_travel_final_project.at_blog.views import blog_page_view, blog_post_view

urlpatterns = [
    path('', blog_page_view, name='blog page'),
    path('blog/<str:slug>', blog_post_view, name='blog post'),
]

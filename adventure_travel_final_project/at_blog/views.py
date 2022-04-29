from django.shortcuts import render

from adventure_travel_final_project.at_blog.models import AdventureTravelPost


def blog_page_view(request):
    posts = AdventureTravelPost.objects.all().order_by('created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_post_view(request, slug):
    post = AdventureTravelPost.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_post.html', context)

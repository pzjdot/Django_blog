from django.shortcuts import render

from assignments.models import About, SocialLink
from blogs.models import Category, Blog


def home(request):

    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    post = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')

    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None

    context = {

        'featured_posts': featured_post,
        'posts': post,
        'about': about,

    }
    return render(request, 'home.html', context)



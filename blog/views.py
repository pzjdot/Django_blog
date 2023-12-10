from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from assignments.models import About, SocialLink
from blog.forms import RegistrationForm
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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form.add_error(None, 'Incorrect information entered')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    context = {
        'form': form

    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')



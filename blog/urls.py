
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from blogs import views as blogs_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>', blogs_view.blogs, name='blogs'),
    path('blogs/search/', blogs_view.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('posts/', views.posts, name='posts'),
    path('logout/', views.logout, name='logout'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>', views.edit_category, name='edit_category'),
    path('delete_category/<int:pk>', views.delete_category, name='delete_category')
]

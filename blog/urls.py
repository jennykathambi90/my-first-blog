from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/draft/', views.post_draft_list, name= 'post_draft_list'),
    path('post/publish/<int:pk>/', views.post_publish, name= 'post_publish'),
    path('post/remove/<int:pk>/', views.post_remove, name='post_remove')
]
from django.urls import path
from . import views

# django find the first url it finds, so we need to specify the app name
app_name = 'blog'

urlpatterns = [
    # the default of '' here is the blog folder
    path('', views.all_blogs, name='all_blogs'),
    # represent the integer as blog ID
    path('<int:blog_id>/', views.detail, name='detail'),
]

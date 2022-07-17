from django.urls import path
from . import views

urlpatterns = [
    # the default of '' here is the blog folder
    path('', views.all_blogs, name='all_blogs'),
]


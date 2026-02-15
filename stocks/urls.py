from django.urls import path  
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('start_analyzing/', views.start_analyzing, name='start_analyzing'),
    path('blog_details/', views.blog_details, name='blog_details'),
]

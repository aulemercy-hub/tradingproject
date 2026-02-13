from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('open_tradingaccount/', views.open_tradingaccount, name='open_tradingaccount'),
    path('pricing/', views.pricing, name='pricing'),
]

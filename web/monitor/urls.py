from django.urls import path
from .views import (
	PostDetailView
	)
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
   	path('post/<pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact')
    ]

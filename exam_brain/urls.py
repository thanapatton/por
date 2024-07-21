from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/', views.readPage, name='read'),
    path('voice1/', views.voice_1, name='voice1'),
]
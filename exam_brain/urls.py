from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/', views.readPage, name='read'),
    path('voice1/', views.voice_1, name='voice1'),
    path('speech/', views.speech, name='speech'),
    path('sent_tokenize/', views.thai_sent_tokenize_view),
    path('test2/', views.test2),
    path('word-tokenize/', views.word_tokenizer, name='word_tokenizer'), 
]
# This file contains the URL patterns for the manim_project application. The URL patterns are used to map URLs to views. The views are the functions that are executed when a user visits a specific URL. The URL patterns are defined using the Django URL dispatcher, which is a Python module that helps to define URL patterns for a Django project. The URL patterns are defined in the urlpatterns list, which is a list of URL patterns. Each URL pattern is defined using the path() function, which takes the URL pattern as the first argument and the view function as the second argument. The URL patterns

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Page d'accueil
    path('edit/', views.edit_code_view, name='edit_code'),  # Page d'édition
    path('generate/', views.generate_video_view, name='generate_video'),  # Page de génération de vidéo
    path('result/', views.result_view , name='result'),  # Page de résultat
    path('generate_pre_coded_video/', views.generate_pre_coded_video_view, name='generate_pre_coded_video'),
    path('video_bank/', views.video_bank_view, name='video_bank'),
]

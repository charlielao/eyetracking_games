from django.urls import path
from . import views

urlpatterns = [
    path('frogger/', views.frogger, name='frogger'),
    path('pacman/', views.pacman, name='pacman'),

]
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokedex/', views.pokedex, name='pokedex'),  
    re_path(r'^.*$', views.index, name='catch_all'),  # Catch-all pattern
]

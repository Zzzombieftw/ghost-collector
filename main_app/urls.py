from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ghost/', views.ghost_index,name='ghost_index'),
    path('ghosts/<int:ghost_id>/', views.ghosts_detail, name='ghost_detail'),

]
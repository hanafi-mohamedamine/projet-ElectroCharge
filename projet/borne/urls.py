from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('borne/', views.liste_bornes),
    path('sessions/', views.sessions),
    path('connecteur/', views.connecteur),
]
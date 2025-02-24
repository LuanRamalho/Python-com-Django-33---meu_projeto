from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.entrar, name='login'),
    path('logout/', views.sair, name='logout'),
    path('home/', views.home, name='home'),
]

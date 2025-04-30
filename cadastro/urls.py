from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.Login_usuario, name='login'),
    path('home/', views.Telainicial_home, name='home'),
]

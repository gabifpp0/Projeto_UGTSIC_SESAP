from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inscricoes/', views.inscricoes, name='inscricoes'),
    path('email/', views.email, name='email')
]
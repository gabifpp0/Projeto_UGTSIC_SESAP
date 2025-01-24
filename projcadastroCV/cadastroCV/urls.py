from django.urls import path
from . import views
urlpatterns =[
    path('', views.index,name='index'),
    path('inscricoes/', views.inscricoes, name='inscricoes')
]
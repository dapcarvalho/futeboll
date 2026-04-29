from django.urls import path
from . import views

urlpatterns = [
    path('times/', views.lista_times, name='lista_times'),
    path('times/novo/', views.criar_time, name='criar_time'),
    path('times/delete/<int:id>/', views.deletar_time, name='deletar_time'),
    path('times/editar/<int:id>/', views.editar_time, name='editar_time'),
]
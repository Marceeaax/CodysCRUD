from django.urls import path
from . import views
from .views import usuario_list


urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('nuevo/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('api/usuarios/', usuario_list, name='usuario-list'),
]

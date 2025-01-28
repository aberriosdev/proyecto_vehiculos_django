from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-vehiculo', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),
    path('registro/', views.signup_view, name='registro'),
    
]

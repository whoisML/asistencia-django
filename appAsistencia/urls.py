from django.urls import path
from . import views

urlpatterns=[
	path('', views.lista_asistencia, name='lista_asistencia'),
	path('usuario/<str:pk>/', views.detalles_usuario, name='detalles_usuario')
]
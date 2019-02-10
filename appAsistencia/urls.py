from django.urls import path
from . import views

urlpatterns=[
	path('', views.lista_asistencia, name='lista_asistencia')
]
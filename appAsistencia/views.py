from django.shortcuts import render, get_object_or_404
from .models import Usuario, Asistencia
from django.utils import timezone

# Create your views here.
def lista_asistencia(request):
	#lista_asistencia = Asistencia.objects.filter(hora_entrada=timezone.now()).order_by('hora_entrada')
	lista_usuarios = Usuario.objects.all()
	return render(request, 'appAsistencia/lista_asistencia.html', {'lista_usuarios':lista_usuarios})

def detalles_usuario(request, pk):
	detalles=get_object_or_404(Usuario, pk=pk)
	return render(request, 'appAsistencia/detalles_usuario.html', {'detalles':detalles})
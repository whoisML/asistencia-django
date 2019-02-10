from django.db import models
from django.utils import timezone
from datetime import timedelta

class Usuario(models.Model):
	nombre = models.CharField(max_length=120, primary_key=True)
	area = models.CharField(max_length=30)
	cargo = models.CharField(max_length=30)

	def registrar_usuario(self):
		self.save()
	def consultar_usuario(self):
		return self

class Asistencia(models.Model):
	nombre = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
	hora_entrada = models.DateTimeField(default=timezone.now)
	hora_ir_a_comer = models.DateTimeField(default=timezone.now)
	hora_regresar_comer = models.DateTimeField(default=timezone.now()+timedelta(hours=1))
	hora_salida = models.DateTimeField(default=timezone.now()+timedelta(hours=8))

	def registrar_asistencia(self):
		self.save()

	def consultar_asistencia(self):
		return self
from django.db import models
# Create your models here.

class Banco(models.Model):
	Nombre = models.CharField(max_length=200)
	Activo = models.BooleanField(default=True)
	def __str__(self):
		return self.Nombre

class TipoTarjeta(models.Model):
	Tipo = models.CharField(max_length=50)
	def __str__(self):
		return self.Tipo

class Tarjeta(models.Model):
	NumTarjeta = models.CharField(max_length=30)
	Banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
	TipoTarjeta = models.ForeignKey(TipoTarjeta, on_delete=models.CASCADE)
	def __str__(self):
		return self.NumTarjeta
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

class Transacciones(models.Model):
	fecha = models.DateTimeField('fecha de cargo')
	descripcion = models.CharField(max_length=150)
	cargo = models.FloatField(default=0.0)
	abono = models.FloatField(default=0.0)
	saldo = models.CharField(max_length=30)
	NumTarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
	def __str__(self):
		return ("%s cargo: %s abono: %s" % (self.fecha,self.cargo,self.abono))
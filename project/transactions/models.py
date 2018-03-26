from django.db import models
from myMovsDisplay.models import Tarjeta

# Create your models here.
class Transaccion(models.Model):
	fecha = models.DateTimeField('fecha de cargo')
	descripcion = models.CharField(max_length=150)
	cargo = models.FloatField(default=0.0)
	abono = models.FloatField(default=0.0)
	saldo = models.CharField(max_length=30)
	NumTarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
	def __str__(self):
		return ("%s cargo: %s abono: %s" % (self.fecha,self.cargo,self.abono))
	class Meta:
		unique_together = ["fecha","descripcion","cargo","abono","saldo"]
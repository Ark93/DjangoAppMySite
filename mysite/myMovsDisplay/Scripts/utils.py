from myMovsDisplay.models import Tarjeta,Transacciones
from  time import strftime, strptime
from datetime import date

def formatTransactionsDate(transacciones_):
	for transaccion in transacciones_:
		transaccion.fecha = transaccion.fecha.date()
	return transacciones_
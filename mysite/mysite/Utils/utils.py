from myMovsDisplay.models import Tarjeta
from transactions.models import Transaccion
from  time import strftime, strptime
from datetime import date
from subprocess import call

def formatTransactionsDate(transacciones_):
	for transaccion in transacciones_:
		transaccion.fecha = transaccion.fecha.date()
	return transacciones_

def startJupyter():
	process_ = call(["jupyter notebook --no-browser"])	
	return process_
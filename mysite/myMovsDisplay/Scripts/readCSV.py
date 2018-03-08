import os
import csv
from  time import strftime, strptime
from django.db import models
from myMovsDisplay.models import Tarjeta,Transacciones

def readFile(numTarjeta):
	q = Tarjeta.objects.get(NumTarjeta='8565')
	count = 0
	path = os.path.join(os.path.abspath(os.pardir),'mysite\myMovsDisplay\Resources')
	for file_ in os.listdir(path):
		print("--" + file_ + "--")
		with open(path + '/' + file_) as f:
			reader_ = csv.reader(f)
			for row in reader_:
				row[0] = strftime('%Y-%m-%d',(strptime(row[0],'%d/%m/%Y')))
				if(row[2]==''): row[2]='0.0'
				if(row[3]==''): row[3]='0.0'
				row[2] = float((row[2].replace(',','')))
				row[3] = float((row[3].replace(',','')))
				t = Transacciones(fecha=row[0], descripcion=row[1], cargo=row[2], abono=row[3], saldo=row[4], NumTarjeta=q)
				previouslyLoaded = Transacciones.objects.filter(fecha==row[0], descripcion==row[1])
				if not previouslyLoaded:
					t.save()
					count =  count+1
				else:
					print("Movimiento Ya existia en DB")
	return count
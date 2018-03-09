import os
import csv
from  time import strftime, strptime
from django.db import models
from myMovsDisplay.models import Tarjeta
from transactions.models import Transaccion
from django.shortcuts import get_object_or_404


def readFile(pk_):
	q = Tarjeta.objects.get(pk=pk_)
	count = 0
	path = os.path.join(os.path.abspath(os.pardir),"mysite\\transactions\Resources")
	for file_ in os.listdir(path):
		if(os.path.isfile(path + '/' + file_) ):
			print("--" + file_ + "--")
			with open(path + '/' + file_) as f:
				reader_ = csv.reader(f)
				for row in reader_:
					fecha_original = row[0]
					row[0] = strftime('%Y-%m-%d',(strptime(row[0],'%d/%m/%Y')))
					if(row[2]==''): row[2]='0.0'
					if(row[3]==''): row[3]='0.0'
					row[2] = float((row[2].replace(',','')))
					row[3] = float((row[3].replace(',','')))
					t = Transaccion(fecha=row[0], descripcion=row[1], cargo=row[2], abono=row[3], saldo=row[4], NumTarjeta=q)
					t.save()
					count =  count+1
					#No double will be loaded due uniqueness
			os.rename(path + '/' + file_, path + '/Cargados/' + str(strftime("%Y-%m-%d_%H-%M-%S")) + ".csv")
	return count
from django.shortcuts import render
from django.http import HttpResponse
import os 
from .Scripts import readCSV
# Create your views here.

def index(request):
	return HttpResponse('You are in the Main page of the App')

def detalles(request, transaccion_id):
	return HttpResponse("Estas viendo los detalles de la transaccion %s." % transaccion_id)

def cargarDatos(request):
	count = readCSV.readFile(8565)
	return HttpResponse("Se Han cargado %s datos" % count)
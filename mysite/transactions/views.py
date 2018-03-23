from django.shortcuts import render
from .models import Transaccion
from django.views import generic
from myMovsDisplay.models import Tarjeta
from mysite.Utils import utils,readCSV
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
class TransactionsView(generic.TemplateView):
	template_name="transactions/Transacciones.html"
	def get_queryset(self):
		"""Return the last five published questions."""
		return utils.formatTransactionsDate(Transaccion.objects.order_by('-fecha'))


class DetailView(generic.DetailView):
	model = Transaccion
	template_name="transactions/detalles.html"

class SeleccionarTarjeta(generic.ListView):
	template_name="transactions/SeleccionarTarjeta.html"
	def get_queryset(self):
		"""Return the last five published questions."""
		return Tarjeta.objects.order_by('-id')

def cargarDatos(request):
	pk_=request.POST['tarjeta']
	count = readCSV.readFile(pk_)
	return HttpResponse("Se cargaron %s records para tarjeta %s" % (count,Tarjeta.objects.get(pk=pk_)))

def Filter(request):
	for key in request.POST:
			print(key)
			value = request.POST[key]
			print(value)
	
	

class FilterView(generic.ListView):
	template_name="transactions/TransaccionesFilt.html"

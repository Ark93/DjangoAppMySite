from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
import os 
from mysite.Utils import utils
from .models import Tarjeta, Banco, TipoTarjeta
from transactions.models import Transaccion

# Create your views here.

class IndexView(generic.TemplateView):
	template_name="myMovsDisplay/Index.html"
	context_object_name = 'context'
	def get_context_data(self,**kwargs):
		"""Return the context dictionary for multiple models. To reference one
		use the key as the object_list"""
		context = super(IndexView, self).get_context_data(**kwargs)
		context["Transacciones"] = utils.formatTransactionsDate(Transaccion.objects.order_by('-fecha')[:10])
		context["Tarjeta"] = Tarjeta.objects.all()[:5]
		return context

class TarjetaDetailView(generic.DetailView):
	model = Tarjeta
	template_name="myMovsDisplay/Tarjeta.html"
	#how to modify date here?

class TarjetaView(generic.ListView):
	template_name="myMovsDisplay/Tarjetas.html"
	#how to modify date here?
	def get_queryset(self):
		"""Return the last five published questions."""
		return Tarjeta.objects.order_by('-Banco')
from django.urls import path
from . import views

app_name='transactions'
urlpatterns = [
	#ex /
	path('',views.TransactionsView.as_view(), name='index'),
	#/filtrados/
	path('filter/',views.Filter, name='filter'),
	#
	path('filtrados/',views.FilterView.as_view(), name='filtrados'),
	#ex /1/
	path('<int:pk>/', views.DetailView.as_view(), name='detalles'),
	#ex /SeleccionarTarjeta/
	path('SeleccionarTarjeta/',views.SeleccionarTarjeta.as_view(), name='selectTarjeta'),
	#ex /SeleccionarTarjeta/1
	path('cargarDatos/',views.cargarDatos, name='cargarDatos')
]
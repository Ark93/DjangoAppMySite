from django.urls import path
from . import views

app_name='myMovsDisplay'
urlpatterns = [
	#ex /myMovsDisplay/
	path('',views.IndexView.as_view(), name='index'),
	#ex /myMovsDisplay/1/
	path('<int:pk>/',views.DetailView.as_view(), name='detalles'),
	#
	path('Tarjeta/',views.TarjetaView.as_view(), name='tarjeta'),
	#
	path('Tarjeta/<int:pk>/',views.TarjetaDetailView.as_view(), name='tarjeta'),
	#
	path('Transacciones/',views.TransactionsView.as_view(), name='transacciones'),
	#
	path('cargarDatos/',views.cargarDatos, name='cargarDatos')
]

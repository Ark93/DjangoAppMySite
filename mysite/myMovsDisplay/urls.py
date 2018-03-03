from django.urls import path
from . import views

app_name='myMovsDisplay'
urlpatterns = [
	#ex /myMovsDisplay/
	path('',views.index, name='index'),
	#ex /myMovsDisplay/1/
	path('<int:transaccion_id>/',views.detalles, name='detalles'),
	#
	path('cargarDatos/',views.cargarDatos, name='cargarDatos')
]

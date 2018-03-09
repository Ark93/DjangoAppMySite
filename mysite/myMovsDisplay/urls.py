from django.urls import path
from . import views

app_name='myMovsDisplay'
urlpatterns = [
	#ex /myMovsDisplay/
	path('',views.IndexView.as_view(), name='index'),
	#
	path('Tarjeta/',views.TarjetaView.as_view(), name='tarjeta'),
	#
	path('Tarjeta/<int:pk>/',views.TarjetaDetailView.as_view(), name='tarjeta'),]

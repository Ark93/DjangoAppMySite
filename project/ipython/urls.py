from django.urls import path
from . import views

app_name='ipython'
urlpatterns = [
	#ex /
	path('',views.embeded, name='index')
]
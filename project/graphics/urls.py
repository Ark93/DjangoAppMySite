from django.urls import path
from . import views

app_name = 'graphics'
urlpatterns = [
	# /graphics/
    path('', views.Graph.as_view(), name='index'),
]
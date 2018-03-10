from django.urls import path
from . import views

app_name = 'graphics'
urlpatterns = [
    path('', views.showimage, name='index'),
]
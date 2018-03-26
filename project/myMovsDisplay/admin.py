from django.contrib import admin
from .models import Banco,TipoTarjeta,Tarjeta

# Register your models here.
admin.site.register(Banco)
admin.site.register(TipoTarjeta)
admin.site.register(Tarjeta)
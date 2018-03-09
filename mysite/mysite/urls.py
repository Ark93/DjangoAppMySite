from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('transactions/', include('transactions.urls')),
    path('myMovsDisplay/', include('myMovsDisplay.urls')),
    path('admin/', admin.site.urls),
]
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('myMovsDisplay/', include('myMovsDisplay.urls')),
    path('admin/', admin.site.urls),
]
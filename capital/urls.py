
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ingresar$', 'app.views.ingresar'),
    url(r'^agente$', 'app.views.agente'),
    url(r'^visita$', 'app.views.visita'),
    url(r'^salir$', 'app.views.salir'),
]

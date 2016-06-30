from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import usuarios
import asignaturas

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('usuarios.urls', namespace='usuarios')),
    url(r'^', include('asignaturas.urls', namespace='asignaturas')),

]

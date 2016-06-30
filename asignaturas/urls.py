from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#	url(r'^calendario', views.crear_calendario, name='calendario'),
    url(r'^courses$', views.user_courses, name='courses'),
    url(r'^disenarcalendario$', views.disenar_calendario, name='disenar_calendario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

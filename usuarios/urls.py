from django.conf.urls import patterns, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.registro, name='registro'),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^profile', views.user_profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

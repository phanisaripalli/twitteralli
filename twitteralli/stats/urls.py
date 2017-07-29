from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.about),
    url(r'^about/$', views.about, name='about'),
    url(r'^about.html$', views.about),
    url(r'^index/$', views.index),
    url(r'^index/$', views.index, name='index'),
    url(r'^tweets/$', views.tweets, name='tweets'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


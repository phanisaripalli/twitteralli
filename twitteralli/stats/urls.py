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
    url(r'^trends/$', views.trends, name='trends'),
    url(r'^foo/$', views.foo, name='foo'),
    url(r'^stream_overview/$', views.stream_overview, name='stream_overview'),
    url(r'^stream_popular_hashtags/$', views.stream_popular_hashtags, name='stream_stream_popular_hashtags'),
    url(r'^stream_minutely_distribution/$', views.stream_minutely_distribution, name='stream_minutely_distribution'),
    url(r'^stream_avg_distribution/$', views.stream_avg_distribution, name='stream_avg_distribution'),



] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


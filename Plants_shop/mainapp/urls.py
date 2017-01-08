from django.conf.urls import url
from .views import main, about, cactus_plants, cactus_genus, cactus_view, error

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^about/$', about, name='about'),
    url(r'^cactus_plants/$', cactus_plants, name='cactus_plants'),
    url(r'^cactus_plants/(\d+)/$', cactus_genus, name='cactus_genus'),
    url(r'^cactus_view/(\d+)/$', cactus_view, name='cactus_view'),
    url(r'^error/$', error, name='error')
]

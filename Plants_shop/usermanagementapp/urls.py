from django.conf.urls import url
from .views import login, logout, registration

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', registration),
]
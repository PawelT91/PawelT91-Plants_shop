from django.conf.urls import url
from .views import admin_main, delete_user, get_user_form, create_user, GensListView, GensDetailView, GensCreateView, \
    GensUpdateView, GensDeleteView, ViewsListView, ViewsDetailView, ViewsCreateView, ViewsUpdateView, ViewsDeleteView


urlpatterns = [
    url(r'^$', admin_main, name='admin_main'),
    url(r'^genus$', GensListView.as_view(), name='genus_view'),
    url(r'^genus/detail/(?P<pk>\d+)/$', GensDetailView.as_view(), name='genus_detail'),
    url(r'^genus/update/(?P<pk>\d+)/$', GensUpdateView.as_view(), name='genus_update'),
    url(r'^genus/delete/(?P<pk>\d+)/$', GensDeleteView.as_view(), name='genus_delete'),
    url(r'^genus/create$', GensCreateView.as_view(), name='genus_create'),

    url(r'^view$', ViewsListView.as_view(), name='genus_view'),
    url(r'^view/detail/(?P<pk>\d+)/$', ViewsDetailView.as_view(), name='view_detail'),
    url(r'^view/update/(?P<pk>\d+)/$', ViewsUpdateView.as_view(), name='view_update'),
    url(r'^view/delete/(?P<pk>\d+)/$', ViewsDeleteView.as_view(), name='view_delete'),
    url(r'^view/create$', ViewsCreateView.as_view(), name='view_create'),

    url(r'^delete/user/(\d+)$', delete_user, name='delete_user'),
    url(r'^get_user_form/(\d+)$', get_user_form),
    url(r'^create/user/(\d*)$', create_user),

]

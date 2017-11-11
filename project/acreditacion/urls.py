from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.AsistenteListaView.as_view(), name='asistente-lista'),
    url(r'^alta/$', views.AsistenteAltaView.as_view(), name='asistente-alta'),
    url(r'^detalle/(?P<pk>\d+)$', views.AsistenteDetalleView.as_view(), name='asistente-detalle'),
    url(r'^modificar/(?P<pk>\d+)$', views.AsistenteModificarView.as_view(), name='asistente-modificar'),
    url(r'^eliminar/(?P<pk>\d+)$', views.AsistenteEliminarView.as_view(), name='asistente-eliminar'),

]

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
)

from . import models, forms


class AsistenteListaView(ListView):
    model = models.Asistente
    template_name = "acreditacion/asistente-lista.html"

#    def get_queryset(self):
#        return models.Asistente.objects.filter(presente=True)


class AsistenteDetalleView(DetailView):
    model = models.Asistente
    template_name = "acreditacion/asistente-detalle.html"


class AsistenteModificarView(UpdateView):
    model = models.Asistente
    form_class = forms.AsistenteModificarForm
    template_name = "acreditacion/asistente-form.html"
    success_url = reverse_lazy('acreditacion:asistente-lista')


class AsistenteAltaView(CreateView):
    model = models.Asistente
    form_class = forms.AsistenteAltaForm
    template_name = "acreditacion/asistente-form.html"
    success_url = reverse_lazy('acreditacion:asistente-lista')


class AsistenteEliminarView(DeleteView):
    model = models.Asistente
    template_name = 'acreditacion/asistente-eliminar.html'
    success_url = reverse_lazy('acreditacion:asistente-lista')

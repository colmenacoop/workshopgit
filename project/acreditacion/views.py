from django.shortcuts import render
from django.views.generic import DetailView

from . import models


class AsistentePresenteView(DetailView):
    model = models.Asistente
    


from django import forms

from . import models


class AsistenteAltaForm(forms.ModelForm):
    class Meta:
        model = models.Asistente
        fields = (
            'nombre', 'apellido', 'dni',
            'email', 'institucion', 'curso'
        )


class AsistenteModificarForm(forms.ModelForm):
    class Meta:
        model = models.Asistente
        fields = AsistenteAltaForm.Meta.fields + ('presente',)


from django.contrib import admin
from django.utils.html import mark_safe

from . import models

# Register your models here.

class AsistenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'presente', 'acreditar')
    search_fields = ('nombre', 'apellido', 'dni')

    def acreditar(self, instance):
        if not instance.presente:
            return mark_safe(
                "<a href='%s' class='button'>Acreditar</a>" % instance.url_set_asistencia()
            )
        


admin.site.register(models.Asistente, AsistenteAdmin)
admin.site.register(models.Curso)
admin.site.register(models.Tutor)
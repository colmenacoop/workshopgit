from django.contrib import admin

from . import models

# Register your models here.

class AsistenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'presente')
    search_fields = ('nombre', 'apellido', 'dni')

admin.site.register(models.Asistente, AsistenteAdmin)
admin.site.register(models.Curso)
admin.site.register(models.Tutor)
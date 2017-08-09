from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Asistente)
admin.site.register(models.Curso)
admin.site.register(models.Tutor)
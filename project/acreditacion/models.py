from django.db import models


class Persona(models.Model):
    """
    """
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)


    def __str__(self):
        return "{} {}".format(self.apellido, self.nombre)

class Tutor(Persona):
    pass


class Curso(models.Model):
    """docstring for Curso"""
    nombre = models.CharField(max_length=50)
    tutor = models.ManyToManyField(Tutor)

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Institucion"
        verbose_name_plural = "Instituciones"

    def __str__(self):
        pass


class Asistente(Persona):

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"

    email = models.CharField(max_length=50)
    # institucion = models.ForeignKey(Institucion)
    institucion = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso)
    presente = models.BooleanField(default=False)
import csv
from acreditacion import models

def borra_todo():
    models.Asistente.objects.all().delete()

def cargar_asistentes():
    ifile  = open('asistentes.csv', "r")
    read = csv.reader(ifile)
    cur = models.Curso.objects.get(pk=1)
    for row in read :
        nombre_completo = row[2].title().split()

        apellido = nombre_completo[-1]
        nombre = ' '.join(nombre_completo[0:-1])
        dni = row[3]
        institucion = row[4]
        # carrera = row[5]
        # mu = row[6]

        models.Asistente.objects.create(apellido=apellido, nombre=nombre, dni=dni, institucion=institucion, curso=cur)
        print(nombre_completo)

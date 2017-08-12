import csv
from acreditacion import models

def borra_todo():
    models.Asistente.objects.all().delete()

def cargar_asistentes():
    with open('asistentes.csv', "r") as ifile:
        read = csv.reader(ifile)
        
        # Obtener docente para el curso.
        if not models.Tutor.objects.exists():
            docente = models.Tutor.objects.create(
                nombre='Docente',
                apellido='Workshop Git',
                dni='00000001'
            )
        else:
            docente = models.Tutor.objects.first()

        # Obtener curso para los asistentes.
        if not models.Curso.objects.exists():
            curso = models.Curso.objects.create(
                nombre='Workshop Git & Github',
            )

            curso.tutor.add(docente)

        else:
            curso = models.Curso.objects.first()


        for row in read :
            nombre_completo = row[2].title().split()

            apellido = nombre_completo[-1]
            nombre = ' '.join(nombre_completo[0:-1])
            dni = row[3]
            institucion = row[4]
            email = row[1]

            asistente = models.Asistente.objects.create(
                apellido=apellido, 
                nombre=nombre, 
                dni=dni,
                email=email, 
                institucion=institucion, 
                curso=curso
            )
            
            print('Se agregó al asistente: %s' % asistente)

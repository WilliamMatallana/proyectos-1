from django.db import models

class Project(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    name = models.CharField(max_length=50, help_text= 'Ingrese el nombre del proyecto')

    def __str__(self):
        return self.name

class Task(models.Model):

    '''
    Modeo que representa una tarea de un proyecto
    '''

    title = models.CharField(max_length=200, help_text='Ingrese el titulo de la tarea')
    description = models.TextField(help_text='Ingrese la descripcion de la tarea')
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + str(self.Project.name)
    

    def __str__(self) -> str:
        return self.title + ' - ' + self.Project.name
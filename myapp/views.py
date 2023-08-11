from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from.models import Project, Task


def index ( request ):
    return HttpResponse("<h1>Index page</h1>") 

def hello( request, username):
    print(username)
    return HttpResponse('Hello %s' % username)

def about( request ):
    return HttpResponse('<h1>About Us</h1>')


def product( request ):
    return HttpResponse('<h1>Product</h1>')

def operacion(request, numero):
        numero_entero = int(numero)
        resultado = (numero_entero + 100) * 2
        return HttpResponse("El resultado es: %s" % resultado)


# Listando todos los proyectos
def projects ( request ):
     projects = list(Project.objects.values())
     return JsonResponse(projects, safe=False)


# Listar una tarea
def tasks ( request, id):
    # task = Task.objects.get(id=id) 
    task = get_object_or_404(Task, id=id)
    return HttpResponse('<h1>Tasks: %s</h1>' % task.title)


# (int)
# Crear una vista que reciba un numero entero que venga como parametro por la url le sume 100 y lo multiplique por 2




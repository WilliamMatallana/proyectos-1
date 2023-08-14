from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask


def index ( request ):
    title = "Django Project!!"
    return render ( request, 'index.html', {
         'title': title
    })

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

def projects ( request ):
     title_projects = "Projects"
     projects = list(Project.objects.values())
     return render ( request, 'projects.html', {
          'title_projects' : title_projects,
          'projects' : projects,
     })

def tasks ( request ):
    tasks = Task.objects.all()
    return render ( request, 'task.html', {'tasks' : tasks})

def create_task(request ):
     if request.method == 'GET':
        return render (request, 'create_task.html',{
          'form' : CreateNewTask()
        })
     else:
        title = request.POST['title']
        description = request.POST['description']
        project_id = 1
        Task.objects.create(title = title, description = description, project_id = project_id)
        return redirect('/task')
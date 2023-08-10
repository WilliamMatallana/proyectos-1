from django.shortcuts import render
from django.http import HttpResponse

def hello( request ):
    return HttpResponse('Hello world')

def about( request ):
    return HttpResponse('<h1>About Us</h1>')


def product( request ):
    return HttpResponse('<h1>Product</h1>')



# Crear una funcion donde se devuelva no solo la cadena de caracteres si no un h1 con la palabra about As, funcion llamada about y crear en url.py crear un nuevo elemento que nos lleve a la pagina de about 

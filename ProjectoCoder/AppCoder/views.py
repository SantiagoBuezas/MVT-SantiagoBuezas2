from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def mostrar_familiares(request):
   return HttpResponse("Hola Mundo")
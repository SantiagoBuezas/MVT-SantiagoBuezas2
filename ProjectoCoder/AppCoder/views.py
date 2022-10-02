from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Familiar

# Create your views here.
def mostrar_familiares(request):
    familiar_1 = Familiar(nombre="Santiago",parentezco="Hijo",edad=31,fecha_de_nacimiento=30/5/1991)
    familiar_2 = Familiar(nombre="Patricia",parentezco="Madre",edad=52,fecha_de_nacimiento=20/9/1962)
    familiar_3 = Familiar(nombre="Jorge",parentezco="Padre",edad=65,fecha_de_nacimiento=25/10/1956)
    contexto = {"familiar_1": familiar_1, "familiar_2":familiar_2,"familiar_3":familiar_3}
    return render(request, "AppCoder/familiares.html",contexto)


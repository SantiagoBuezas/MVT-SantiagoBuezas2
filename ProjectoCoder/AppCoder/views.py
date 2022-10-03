from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Familiar

# Create your views here.
def mostrar_familiares(request):
    familiar_1 = Familiar(nombre="Santiago",parentezco="Hijo",edad=31,fecha_de_nacimiento="1991-5-30")
    familiar_2 = Familiar(nombre="Patricia",parentezco="Madre",edad=52,fecha_de_nacimiento="1962-5-25")
    familiar_3 = Familiar(nombre="Jorge",parentezco="Padre",edad=65,fecha_de_nacimiento="1965-7-20")
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    contexto = {"familiar_1": familiar_1, "familiar_2":familiar_2,"familiar_3":familiar_3}
    return render(request, "AppCoder/familiares.html",contexto)


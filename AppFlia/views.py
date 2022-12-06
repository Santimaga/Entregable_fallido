from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse 
# Create your views here.

def integrante(request):

# nacimiento = 18/12/1958
    Familiar1 = Familiares(nombre ="Eduardo", apellido = "Magarinos", edad = 68 , con_vida = False)
    Familiar1.save()
    cadena1 = f"Los integrantes de mi familia son: {Familiar1.nombre}, {Familiar1.apellido}"

    return HttpResponse(cadena1)

    """ Familiar2 =Familiares(nombre ="Andrea", apellido = "Menghi", nacimiento = "28/04/64", edad = 58 , con_vida = True)
    Familiar3 =Familiares(nombre ="Santiago", apellido = "Magarinos", nacimiento = "28/10/95", edad = 27 , con_vida = True)
    Familiar4 =Familiares(nombre ="Agustin", apellido = "Magarinos", nacimiento = "21/05/98", edad = 24 , con_vida = True)
    Familiar5 =Familiares(nombre ="Gonzalo", apellido = "Magarinos", nacimiento = "28/05/98", edad = 24 , con_vida = True)


    Familiar.save()
    cadena1 = f"Los integrantes de mi familia son: {Familiar1.nombre}, {Familiar1.apellido}"
    cadena2 = f"Los integrantes de mi familia son: {Familiar2.nombre}, {Familiar2.apellido}"
    cadena3 = f"Los integrantes de mi familia son: {Familiar3.nombre}, {Familiar3.apellido}"
    cadena4 = f"Los integrantes de mi familia son: {Familiar4.nombre}, {Familiar4.apellido}"
    cadena5 = f"Los integrantes de mi familia son: {Familiar5.nombre}, {Familiar5.apellido}"
    return HttpResponse(cadena1)
    return HttpResponse(cadena2)
    return HttpResponse(cadena3)
    return HttpResponse(cadena4)
    return HttpResponse(cadena5)
"""


from django.http import HttpResponse
from django.template import Template, Context, loader

#Las views son funciones.

def saludar (request):
    return HttpResponse("Hola mundo")

def segunda_vista(request):
    return HttpResponse("Ya entendiii creo que esta funcionando")

"""def html(request):
    
    Dic = {"Nombre":"Juan","Apellido":"Perez","Rol":"Padre","Edad":45,"Nacimiento":"10/10/77", "Familiares":["juan","ana","pepe"]}

    web = open("D:/SANTIAGO/CODER/Curso coder Python/Proyecto entregable/virtual/EntregableCoder/Plantillas/template1.html")
    #Repasar Clase 8
    template = Template(web.read())
    web.close()
    contexto = Context(Dic)

    documento = template.render(contexto)#llena los espacios vacios con el contexto.
    return HttpResponse(documento)"""

def html(request):
    Dic = {"Nombre":"Juan","Apellido":"Perez","Rol":"Padre","Edad":45,"Nacimiento":"10/10/77", "Familiares":["juan","ana","pepe"]}

    template = loader.get_template("template1.html")
    documento = template.render(Dic)#llena los espacios vacios con el contexto.
    
    return HttpResponse(documento)

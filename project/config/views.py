from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola")

def saludo2(request):
    nombre = input ("Ingrese su nombre")
    return HttpResponse(f"Hola {nombre}")
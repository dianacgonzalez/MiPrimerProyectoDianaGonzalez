from django.shortcuts import redirect, render

# Create your views here.
from . import models
from . import forms

def index(request):
    return render(request, "entrega3/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "entrega3/profesor_list.html", contexto)

def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = forms.ProfesorForms()
    return render(request, "entrega3/profesor_create.html", {"form": form})

def estudiante_list(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"estudiante": consulta}
    return render(request, "entrega3/estudiante_list.html", contexto)

def estudiante_create(request):
    if request.method == "POST":
        form = forms.EstudianteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = forms.EstudianteForms()
    return render(request, "entrega3/estudiante_create.html", {"form": form})

def curso_list(request):
    consulta = models.Curso.objects.all()
    contexto = {"curso": consulta}
    return render(request, "entrega3/curso_list.html", contexto)

def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:
        form = forms.CursoForms()
    return render(request, "entrega3/curso_create.html", {"form": form})
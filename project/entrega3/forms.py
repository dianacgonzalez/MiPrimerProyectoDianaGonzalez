from django import forms

from . import models

class ProfesorForms(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"

class EstudianteForms(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = "__all__"

class CursoForms(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"
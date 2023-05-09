from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=164)
    comision = forms.IntegerField(required=True, max_value=5000)
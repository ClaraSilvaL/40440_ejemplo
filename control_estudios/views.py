from django.shortcuts import render

# Create your views here.
def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel"},
            {"nombre": "Ivan", "apellido": "Tomasevich"},
            {"nombre": "Carlos", "apellido": "Perez"},
            {"nombre": "Manuela", "apellido": "Gomez"},
        ]
    }
    http_response = render(
        request = request,
        template_name='control_estudios/lista_estudiantes.html',
        context = contexto,
    )
    return http_response
    
def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre": "Python", "comision": "40440"},
            {"nombre": "Frontend", "comision": "40441"},
            {"nombre": "Diseño", "comision": "40442"},
        ]
    }
    http_response = render(
        request = request,
        template_name='control_estudios/lista_cursos.html',
        context = contexto,
    )
    return http_response
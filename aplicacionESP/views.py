from aplicacionESP import serializers
from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .serializers import MemberSerializer
from .models import Profile

# Create your views here.

def inicio(request):
    
    arduino_history = Profile.objects.all().order_by('id')
    datos = {
        'perfil': arduino_history,
        #'group_name_singular' : pluralToSingular(group_name),
        #'cursos' : cursos,
        #'enrolled_courses' : enrolled_courses,
        #'enrolled_calificaciones' : enrolled_calificaciones,
        }

    if request.method == 'POST':
        # Procesa los datos recibidos del ESP8266

        # Realiza las acciones necesarias con los datos

        # Retorna una respuesta simple al ESP8266

        
        template = loader.get_template('inicio.html')
        return HttpResponse(template.render(datos, request))
    else:
        template = loader.get_template('inicio.html')
        return HttpResponse(template.render(datos, request))

    

    
    
        
    
    



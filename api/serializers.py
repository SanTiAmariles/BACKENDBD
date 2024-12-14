from rest_framework import serializers
from .models import Estudiante, Profesor

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'correoInstitucional', 'numeroCelular',  'password', 'codigoEstudiante','codigoEstudiante']


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['documento', 'direccion', 'email', 'password', 'photo']

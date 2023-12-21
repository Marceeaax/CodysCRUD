from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre_apellido', 'correo_electronico', 'telefono', 'fecha_nacimiento', 'foto_perfil']

from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto_perfil', 'nombre_apellido', 'correo_electronico', 'telefono', 'fecha_nacimiento']

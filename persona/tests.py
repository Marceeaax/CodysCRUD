from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Asume que el archivo 'Ejemplo1.png' está en la carpeta 'media/fotos_ejemplos' dentro de tu proyecto
        image_path = 'media/fotos_ejemplos/Ejemplo1.png'
        image = SimpleUploadedFile(name='Ejemplo1.png',
                                   content=open(image_path, 'rb').read(),
                                   content_type='image/png')
        self.usuario_data = {
            'nombre_apellido': 'Test User',
            'correo_electronico': 'test@example.com',
            'telefono': '123456789',
            'fecha_nacimiento': '2000-01-01',
            'foto_perfil': image  # Añade la imagen al conjunto de datos
        }
        self.response = self.client.post(
            reverse('usuario-list'),
            self.usuario_data,
            format="multipart"  # Usa 'multipart' en lugar de 'json' para datos que incluyen archivos
        )
        
    def test_api_can_create_a_usuario(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

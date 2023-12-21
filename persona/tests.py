from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario_data = {'nombre_apellido': 'Test User', 'correo_electronico': 'test@example.com', 'telefono': '123456789', 'fecha_nacimiento': '2000-01-01'}
        self.response = self.client.post(
            reverse('usuario-list'),
            self.usuario_data,
            format="json")
        print(self.response)

    def test_api_can_create_a_usuario(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

from django.db import models

class Usuario(models.Model):
    foto_perfil = models.ImageField(upload_to='fotos_perfiles/')
    nombre_apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre_apellido

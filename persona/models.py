from django.db import models
from datetime import date
from PIL import Image

class Usuario(models.Model):
    foto_perfil = models.ImageField(upload_to='fotos_perfiles/')
    nombre_apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.foto_perfil.path)
        output_size = (100, 100)  # Tamaño deseado
        img.thumbnail(output_size)
        img.save(self.foto_perfil.path)

    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
    
    def __str__(self):
        return self.nombre_apellido


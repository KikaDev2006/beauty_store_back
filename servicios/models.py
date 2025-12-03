from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.DurationField()
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)  # True for available, False for unavailable

    def __str__(self):
        return self.nombre

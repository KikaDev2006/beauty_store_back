from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)  # True for available, False for unavailable
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    id_categoria = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE, related_name='productos')
    def __str__(self):
        return self.nombre
    
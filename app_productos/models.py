from django.db import models

class Producto(models.Model):
    ID_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=50, verbose_name="Unidad de Medida (Ej: kg)")

    def __str__(self):
        return f"{self.nombre} ({self.ID_producto})"

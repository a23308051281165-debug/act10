from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('ID_producto', 'nombre', 'precio', 'stock', 'categoria', 'unidad_medida')
    search_fields = ('nombre', 'categoria')

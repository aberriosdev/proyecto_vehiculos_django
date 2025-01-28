from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'fecha_creacion')
    list_filter = ('marca', 'categoria')
    search_fields = ('modelo', 'serial_carroceria', 'serial_motor')


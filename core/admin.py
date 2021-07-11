from django.contrib import admin
from .models import Cliente,Usuario,Producto,Venta

# Register your models here.
# Permite manejar o manipular el modelo por completo.
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Venta)
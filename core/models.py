from django.db import models

# Create your models here.

class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name="Id Categoria")
    suscripcion = models.BooleanField(default=False, verbose_name="Suscripcion")

    def _str_(self):
        return self.idCliente

# modelo usuario

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="Id Usuario")
    username = models.CharField(max_length=20, null=True, blank=True, verbose_name="nombre usuario")
    password = models.CharField(max_length=20, null=True, blank=True, verbose_name="Modelo")
    idCliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def _str_(self):
        return self.idUsuario

# modelo producto

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id Usuario")
    nProducto = models.CharField(max_length=30, null=True, blank=True, verbose_name="nombre producto")
    precio = models.IntegerField(max_length=20, null=True, blank=True, verbose_name="precio producto")
    cantidad = models.IntegerField(max_length=10, null=True, blank=True, verbose_name="cantidad producto")
    descripcion = models.CharField(max_length=20, null=True, blank=True, verbose_name="descripcion producto")
    idVenta= models.ForeignKey(Venta, on_delete=models.CASCADE)

    def _str_(self):
        return self.idProducto

class Venta(models.Model):
    idVenta = models.IntegerField(primary_key=True, verbose_name="Id Usuario")
    tVenta = models.IntegerField(max_length=10, null=True, blank=True, verbose_name="total venta")
    idCliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def _str_(self):
        return self.idVenta


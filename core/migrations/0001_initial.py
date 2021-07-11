# Generated by Django 3.2.3 on 2021-07-11 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Categoria')),
                ('suscripcion', models.BooleanField(default=False, verbose_name='Suscripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Usuario')),
                ('tVenta', models.IntegerField(blank=True, null=True, verbose_name='total venta')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Usuario')),
                ('username', models.CharField(blank=True, max_length=20, null=True, verbose_name='nombre usuario')),
                ('password', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Usuario')),
                ('nProducto', models.CharField(blank=True, max_length=30, null=True, verbose_name='nombre producto')),
                ('precio', models.IntegerField(blank=True, null=True, verbose_name='precio producto')),
                ('cantidad', models.IntegerField(blank=True, null=True, verbose_name='cantidad producto')),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True, verbose_name='descripcion producto')),
                ('idVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta')),
            ],
        ),
    ]

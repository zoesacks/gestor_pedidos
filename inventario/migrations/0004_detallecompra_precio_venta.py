# Generated by Django 4.2.7 on 2023-12-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_remove_compra_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='precio_venta',
            field=models.IntegerField(default=0),
        ),
    ]

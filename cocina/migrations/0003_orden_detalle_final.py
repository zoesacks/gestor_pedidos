# Generated by Django 4.2.7 on 2023-12-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocina', '0002_remove_subrecetareceta_receta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='detalle_final',
            field=models.TextField(default='No terminado'),
        ),
    ]
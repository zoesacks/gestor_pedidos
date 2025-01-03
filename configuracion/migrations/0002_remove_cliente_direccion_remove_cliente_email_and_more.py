# Generated by Django 4.2.7 on 2024-01-09 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Direccion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='UltimaModificacion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Usuario',
        ),
        migrations.AddField(
            model_name='cliente',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='HabitosDiarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alimentacion', models.CharField(blank=True, choices=[('Saludable', 'Saludable'), ('No saludable', 'No saludable'), ('Variado', 'Variado')], max_length=255, null=True)),
                ('hidratacion', models.CharField(blank=True, choices=[('Nada', 'Nada'), ('Menos de 2lt', 'Menos de 2lt'), ('Más de 2lt', 'Más de 2lt')], max_length=255, null=True)),
                ('alcohol', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No'), ('Ocasionalmente', 'Ocasionalmente')], max_length=255, null=True)),
                ('fuma', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No'), ('Ocasionalmente', 'Ocasionalmente')], max_length=255, null=True)),
                ('cuantos_cigarrillos', models.PositiveIntegerField(blank=True, null=True)),
                ('actividad_fisica', models.BooleanField(default=False)),
                ('cuantos_dias_actividad_fisica', models.PositiveIntegerField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DatosClinicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alergias', models.BooleanField(default=False)),
                ('cuales_alergias', models.CharField(blank=True, max_length=255, null=True)),
                ('medicaciones', models.CharField(blank=True, max_length=255, null=True)),
                ('marcapasos', models.BooleanField(default=False)),
                ('presion_arterial', models.BooleanField(default=False)),
                ('presion_arterial_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('diabetes', models.BooleanField(default=False)),
                ('diabetes_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('colesterol', models.BooleanField(default=False)),
                ('colesterol_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('estres', models.BooleanField(default=False)),
                ('estres_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('depresion', models.BooleanField(default=False)),
                ('depresion_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('ansiedad', models.BooleanField(default=False)),
                ('ansiedad_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('insomnio', models.BooleanField(default=False)),
                ('insomnio_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('hiper_hipo_tiroidismo', models.BooleanField(default=False)),
                ('hiper_hipo_tiroidismo_medicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('horas_descanso', models.CharField(blank=True, max_length=255, null=True)),
                ('ciclo_menstrual', models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Irregular', 'Irregular')], max_length=255, null=True)),
                ('infecciones_infectocontagiosas', models.BooleanField(default=False)),
                ('infecciones_infectocontagiosas_cual', models.CharField(blank=True, max_length=255, null=True)),
                ('celiaquia', models.BooleanField(default=False)),
                ('colon_irritable', models.BooleanField(default=False)),
                ('intolerancia_gastrica', models.BooleanField(default=False)),
                ('gastritis', models.BooleanField(default=False)),
                ('intolerancia_lactosa', models.BooleanField(default=False)),
                ('asma', models.BooleanField(default=False)),
                ('broncoespasmo', models.BooleanField(default=False)),
                ('epoc', models.BooleanField(default=False)),
                ('anticonceptivos', models.BooleanField(default=False)),
                ('hormonas', models.BooleanField(default=False)),
                ('anticoagulantes', models.BooleanField(default=False)),
                ('analgesicos', models.BooleanField(default=False)),
                ('corticoides', models.BooleanField(default=False)),
                ('complejo_vitaminico', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.cliente')),
            ],
            options={
                'verbose_name': 'datos clinicos',
                'verbose_name_plural': 'datos clinicos',
            },
        ),
        migrations.CreateModel(
            name='CuidadosDeLaPiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('se_higieniza_habitualmente', models.BooleanField(default=False)),
                ('se_exfolia', models.CharField(blank=True, choices=[('No', 'No'), ('Una vez por semana', 'Una vez por semana'), ('Cada 15 días', 'Cada 15 días'), ('Una vez al mes', 'Una vez al mes')], max_length=255, null=True)),
                ('usa_maquillaje', models.BooleanField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No'), ('Ocasionalmente', 'Ocasionalmente')], max_length=255, null=True)),
                ('utiliza_cremas', models.BooleanField(default=False)),
                ('cuales_cremas', models.CharField(blank=True, max_length=255, null=True)),
                ('protector_solar', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.cliente')),
            ],
        ),
    ]

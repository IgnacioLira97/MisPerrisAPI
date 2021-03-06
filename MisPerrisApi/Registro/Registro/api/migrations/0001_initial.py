# Generated by Django 2.1.2 on 2018-11-30 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idCiudad', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('foto', models.FileField(upload_to='media')),
                ('descripcion', models.CharField(max_length=255)),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('idRaza', models.IntegerField(primary_key=True, serialize=False)),
                ('Raza', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tipoVivienda',
            fields=[
                ('idTipo', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('run', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('correo', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=9)),
                ('password', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=150)),
                ('tipoVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoVivienda')),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Raza'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='idRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Region'),
        ),
    ]

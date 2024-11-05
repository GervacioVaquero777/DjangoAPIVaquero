# Generated by Django 5.1.2 on 2024-11-05 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_perfillaboral_delete_usuariodetalles'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilLaboral',
            fields=[
                ('id_oficio', models.AutoField(primary_key=True, serialize=False)),
                ('oficio', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('experiencia_laboral', models.PositiveIntegerField()),
                ('calificacion', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'perfil_laboral',
            },
        ),
        migrations.CreateModel(
            name='UsuarioDetalles',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField(default=0)),
                ('password', models.CharField(default='default_password', max_length=255)),
                ('correo', models.EmailField(default='example@example.com', max_length=254, unique=True)),
                ('imagen_url', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'detalles_usuario',
            },
        ),
    ]
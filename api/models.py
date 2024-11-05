from django.db import models

# Create your models here.
class Generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    tipo_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"
        
    
class Usuarios(models.Model):
    usuarios_id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Generos,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "usuarios"   
        
class UsuarioDetalles(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono = models.BigIntegerField(default=0)
    password = models.CharField(max_length=255, default="default_password")
    correo = models.EmailField(unique=True, default="example@example.com")
    imagen_url = models.URLField(max_length=255)
    

    class Meta:
        db_table = "detalles_usuario"
        
class PerfilLaboral(models.Model):
    id_oficio = models.AutoField(primary_key=True)  # Establece un ID único para cada registro
    oficio = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    experiencia_laboral = models.PositiveIntegerField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "perfil_laboral"

class Habilidad(models.Model):
    trabajador = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='habilidades', limit_choices_to={'tipo_usuario': 'TRABAJADOR'})
    habilidad = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)  # Ejemplo: 'Básico', 'Intermedio', 'Avanzado'

    class Meta:
        db_table = "habilidades"

class Disponibilidad(models.Model):
    trabajador = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='disponibilidad', limit_choices_to={'tipo_usuario': 'TRABAJADOR'})
    dia = models.CharField(max_length=20)  # Ejemplo: 'Lunes', 'Martes', etc.
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = "disponibilidad"



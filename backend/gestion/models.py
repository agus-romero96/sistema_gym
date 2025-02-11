from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date

def validar_cedula(value):
    """Valida que la cédula tenga exactamente 10 dígitos numéricos."""
    if len(value) != 10:
        raise ValidationError("La cédula debe tener exactamente 10 dígitos.")
    if not value.isdigit():
        raise ValidationError("La cédula debe contener solo dígitos numéricos.")

def validar_telefono(value):
    """Valida que el teléfono tenga exactamente 10 dígitos numéricos."""
    if len(value) != 10:
        raise ValidationError("El teléfono debe tener exactamente 10 dígitos.")
    if not value.isdigit():
        raise ValidationError("El teléfono debe contener solo dígitos numéricos.")


letras_validator = RegexValidator(
    regex=r'^[a-zA-ZÀ-ÿ\s]+$',
    message="Este campo solo puede contener letras y espacios."
)

ESTADO_CLASE_CHOICES = (
    ('P', 'Programada'),
    ('C', 'Cancelada'),
    ('F', 'Finalizada'),
)

class Persona(models.Model):
    nombre = models.CharField(max_length=50, validators=[letras_validator])
    apellido = models.CharField(max_length=50, validators=[letras_validator])
    cedula = models.CharField(max_length=10, primary_key=True, validators=[validar_cedula])
    email = models.EmailField()
    telefono = models.CharField(max_length=10, validators=[validar_telefono])
    direccion = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.cedula} -- {self.nombre} {self.apellido}"


class Cliente(Persona):
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return super().__str__()


class Instructor(Persona):
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'instructor'
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'

    def __str__(self):
        return super().__str__()


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.IntegerField(verbose_name="Duración en minutos")
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    participantes = models.ManyToManyField('Cliente', related_name="clases", blank=True)
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CLASE_CHOICES,
        default='P',
        help_text="Estado de la clase: Programada, Cancelada o Finalizada."
    )

    class Meta:
        db_table = 'clase'
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora} - {self.get_estado_display()}"
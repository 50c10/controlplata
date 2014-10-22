from django.db import models

# Create your models here.
class Solisitud(models.Model):
	fecha_recepcion = models.DateField()
	nombre = models.CharField(max_length=200)
	municipio = models.CharField(max_length=20)
	actividad = models.CharField(max_length=80) 
	monto = models.DecimalField(max_digits=11, decimal_places=2)
	sector = models.CharField(max_length=80)
	programa = models.CharField(max_length=200)
	analista = models.CharField(max_length=80)
	estatus = models.CharField(max_length=20)
	fecha_asignacion = models.DateField('date published')
	comite = models.CharField(max_length=80)
	fecha_comite = models.DateField('date published')
	recibio_expediente = models.CharField(max_length=80)
	observaciones = models.CharField(max_length=300)
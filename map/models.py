from django.db import models
from . import constants


# Create your models here.

class Predio(models.Model):

	nombre = models.CharField(max_length=30 , blank=False)
	vendedor = models.CharField(max_length=50, blank=True)
	fecha_adquisicion = models.CharField(max_length=30, blank=True)
	valor = models.FloatField(default = 0.0)
	plan_manejo = models.CharField(max_length=100, blank=True)
	catastro = models.CharField(max_length=25)
	escritura = models.CharField(max_length=25)
	area = models.FloatField( verbose_name=u'area (Ha)')
	corregimiento = models.CharField(max_length=25 , choices=constants.CORREGIMIENTOS)
	vereda = models.CharField(max_length=25 , choices= constants.VEREDAS)
	latitude = models.FloatField(default= 0.0)
	longitude = models.FloatField(default=0.0)
	cuenca = models.CharField(max_length=25 , choices=constants.CUENCAS)
	sub_cuenca = models.CharField(max_length=25 , choices=constants.SUB_CUENCAS)
	temperatura_promedio= models.FloatField(default = 0.0)
	via_pavimentada = models.FloatField(default = 0.0)
	via_destapada = models.FloatField(default = 0.0)
	via_trocha = models.FloatField(default = 0.0)
	protegido = models.BooleanField()
	numero_acta = models.CharField(max_length=25, blank=True)
	fecha_acta = models.CharField(max_length=25, blank=True)
	observaciones = models.TextField(blank=True)
	url = models.URLField(default="",  blank=True)
	ecosistema = models.CharField(max_length=50 , blank=True)
	zona_de_vida = models.CharField(max_length=50, blank=True)
	altura_max = models.CharField(max_length=25, blank=True)
	altura_min = models.CharField(max_length=25, blank=True)
	clima = models.CharField(max_length=25 ,blank=True)
	suelos = models.CharField(max_length=25,blank=True)
	relieve = models.CharField(max_length=50, blank=True)
	clase_agrologica = models.CharField(max_length=25 , blank=True)



	def __str__(self):
		return ( "%s") % (self.nombre)

	def save(self, *args, **kwargs):

		if not self.protegido:
			self.numero_acta="NO PROTEGIDO"
			self.fecha_acta="NO PROTEGIDO"
			self.protegido = False
		return super(Predio, self).save(*args, **kwargs)



class Nacimiento(models.Model):
	
	nacimiento = models.CharField(max_length=25, default='')
	caudal = models.FloatField(default = 0.0)
	color = models.IntegerField(default=0)
	ph = models.FloatField (default=0.0)
	turbiedad = models.FloatField(default= 0.0)
	dureza = models.FloatField(default=0.0)
	sulfatos = models.FloatField(default = 0.0)
	nitratos = models.FloatField(default = 0.0)
	temperatura = models.FloatField(default = 0.0)
	dbo = models.FloatField(default = 0.0)
	solidos = models.FloatField(default = 0.0)
	dqo = models.FloatField(default = 0.0)
	coliformes = models.FloatField(default = 0.0)
	altura = models.IntegerField(max_length=25 )
	predio = models.ForeignKey(Predio)
	latitude = models.FloatField(default= 0.0)
	longitude = models.FloatField(default=0.0)

	def __str__(self):
		return ("%s - %s") %(self.id, self.predio.nombre)
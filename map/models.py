from django.db import models
from . import constants


# Create your models here.

class Predio(models.Model):


	catastro = models.CharField(max_length=25)
	escritura = models.CharField(max_length=25)
	area = models.IntegerField()
	corregimiento = models.CharField(max_length=25 , choices=constants.CORREGIMIENTOS)
	vereda = models.CharField(max_length=25 , choices= constants.VEREDAS)
	latitude = models.FloatField(default= 0.0)
	longitude = models.FloatField(default=0.0)
	cuenca = models.CharField(max_length=25 , choices=constants.CUENCAS)
	sub_cuenca = models.CharField(max_length=25 , choices=constants.SUB_CUENCAS)
	temperatura = models.FloatField(default = 0.0)
	presion_antropica = models.CharField(max_length=25 , choices=constants.PRESION)
	photo = models.ImageField(blank=True)
	via_pavimentada = models.FloatField(default = 0.0)
	via_destapada = models.FloatField(default = 0.0)
	via_trocha = models.FloatField(default = 0.0)

	def __str__(self):
		return ("%s - %s") % (self.catastro , self.vereda)



class Nacimiento(models.Model):
	
	
	photo = models.ImageField(blank=True)
	vegetable_photo = models.ImageField(blank=True)
	caudal = models.FloatField(default = 0.0)
	ph = models.FloatField (default=0.0)
	color = models.CharField(max_length=25 , choices=constants.COLOR)
	turbiedad = models.FloatField(default= 0.0)
	dureza = models.FloatField(default=0.0)
	sulfatos = models.FloatField(default = 0.0)
	nitratos = models.FloatField(default = 0.0)
	temperatura = models.FloatField(default = 0.0)
	dbo = models.FloatField(default = 0.0)
	solidos = models.FloatField(default = 0.0)
	dqo = models.FloatField(default = 0.0)
	coliformes = models.FloatField(default = 0.0)
	cabecera_municipal = models.CharField(max_length=25 , choices=constants.CABECERA)
	topo_especificacion = models.CharField(max_length=25 , choices=constants.TOPO_ESPECIFICACION)
	altura = models.IntegerField(max_length=25 )
	predio = models.ForeignKey(Predio)
	latitude = models.FloatField(default= 0.0)
	longitude = models.FloatField(default=0.0)

	def __str__(self):
		return ("%s - %s") %(self.cabecera_municipal , self.predio.catastro)
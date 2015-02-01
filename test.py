# Full path and name to your csv file
csv_filepathname="/home/arce/sihy/test.csv"
# Full path to your django project directory
your_djangoproject_home="/home/arce/sihy"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'appHidrica.settings'

from map.models import Nacimiento , Predio
import django
django.setup()

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

for row in dataReader:
	if row[0] != 'Identificador': # Ignore the header row, import everything else
		zipcode = Nacimiento()
		zipcode.identificador = row[0]
		zipcode.predio = Predio.objects.get(nombre=row[1])
		zipcode.latitude = row[2]
		zipcode.longitude = row[3]
		zipcode.caudal = row[4]
		zipcode.ph = row[5]
		zipcode.color = row[6]
		zipcode.turbiedad = row[7]
		zipcode.dureza = row[8]
		zipcode.sulfatos = row[9]
		zipcode.nitratos = row[10]
		zipcode.temperatura = row[11]
		zipcode.dbo = row[12]
		zipcode.solidos = row[13]
		zipcode.dqo =  row[14]
		zipcode.coliformes = row[15]
		zipcode.altura = row[16]
		zipcode.save()
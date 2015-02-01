# Full path and name to your csv file

csv_filepathname="C:\sihy\appHidrica\test.csv"

# Full path to your django project directory

your_djangoproject_home="C:\sihy\appHidrica"

 

import sys,os

sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


from map.models import Predio

 

import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

 

for row in dataReader:

	if row[0] != 'Predio': # Ignore the header row, import everything else

		zipcode = Predio()

		zipcode.nombre = row[0]

		zipcode.catastro = row[1]

		zipcode.escritura = row[2]

		zipcode.area = row[3]

		zipcode.corregimiento[4]
		zipcode.vereda = row[5]
		zipcode.latitude = row[6]
		zipcode.longitude = row[7]
		zipcode.cuenca = row[8]
		zipcode.sub_cuenca = row[9]
		zipcode.temperatura = row[10]
		zipcode.via_pavimentada = row[11]
		zipcode.via_destapada = row[12]
		zipcode.via_trocha = row[13]

		zipcode.save()
from django.shortcuts import render
import json
from .models import Predio , Nacimiento
from endless_pagination.views import AjaxListView
from django.views.generic.list import ListView
from django.core.paginator import Paginator


class MapView(ListView):
	template_name = 'map.html'
	queryset = Predio.objects.all()

	
	def get_context_data(self , **kwargs):
		context = super(MapView, self).get_context_data(**kwargs)
  		context['object_list_json'] = self.get_json_results()
  		context['json_object_list'] = self.get_json()
  		context['max_area'] = self.get_highest_area()
  		context['max_source'] = self.get_highest_source()
  		context['max_volume'] = self.get_highest_volume()
  		context['max_pressure'] = self.get_highest_pressure()
  		context['min_area'] = self.get_smallest_area()
  		context['min_source'] = self.get_smallest_source()
  		context['min_volume'] = self.get_smallest_volume()
  		context['min_pressure'] = self.get_smallest_source()

 		return context
	def get_json_results(self):
	        items = []
	        for item in self.object_list:
	            items.append({
	                'latitude': item.latitude if item.latitude else None,
	                'longitude': item.longitude if item.longitude else None,
	                'catastro' : item.catastro,
					'escritura': item.escritura,
					'area': item.area,
					'corregimiento': item.corregimiento,
					'vereda': item.vereda,
					'cuenca': item.cuenca,
					'sub_cuenca': item.sub_cuenca,
					'temperatura': item.temperatura,
					'presion_antropica': item.presion_antropica,
					'via_pavimentada': item.via_pavimentada,
					'via_destapada': item.via_destapada,
					'via_trocha': item.via_trocha,
					'id' : item.id , 
					'photo' : item.photo.url ,
	                })
	            
	        return json.dumps(items)

	def get_json(self):
		val = Nacimiento.objects.all()
		p = Paginator(val, 1)
		
		items = []
		for item in p.object_list:
			items.append({
				'caudal' : item.caudal,
				'ph' : item.ph,
				'color' : item.color,
				'turbiedad' : item.turbiedad,
				'dureza' : item.dureza,
				'sulfatos' : item.sulfatos,
				'nitratos' : item.nitratos,
				'temperatura' : item.temperatura,
				'dbo' : item.dbo,
				'solidos' : item.solidos,
				'dqo' : item.dqo,
				'coliformes' : item.coliformes,
				'predio' : item.predio.id ,
				'cabecera_municipal' : item.cabecera_municipal, 
				'topo_especificacion' : item.topo_especificacion,
				'altura' : item.altura,
				'latitude' : item.latitude,
				'longitude' : item.longitude,
				})
		return json.dumps(items)

############################################################################
	def get_highest_area(self):
		highest = self.object_list[0]
		for item in self.object_list:
			if item.area > highest.area:
				highest = item

		return highest

	
	def get_highest_source(self):
		queryset = self.object_list
		source_queryset = Nacimiento.objects.all()
		highest = queryset[0]
		count = 0
		
		for predio in queryset:
			aux = count
			count = 0
			
			for source in source_queryset:
				if source.predio == predio:
					count = count + 1
										
			if count > aux:
				highest = predio
					
		return highest

	def get_highest_volume(self):
		queryset = self.object_list
		source_queryset = Nacimiento.objects.all()
		highest = source_queryset[0]
		caudal = 0

		for predio in queryset:
			aux = caudal
			caudal = 0

			for source in source_queryset:
				if source.predio == predio:
					caudal = caudal+ source.caudal

			if caudal > aux:
				highest = predio

		return highest


	def get_highest_pressure(self):
		
		highest = self.object_list[0]

		for item in self.object_list:
			if item.presion_antropica > highest.presion_antropica:
				highest = item

		return highest

#############################################################################
					
	def get_smallest_area(self):
		smallest = self.object_list[0]
		for item in self.object_list:
			if item.area < smallest.area:
				smallest = item
		return smallest

			
	def get_smallest_source(self):
			queryset = self.object_list
			source_queryset = Nacimiento.objects.all()
			smallest = queryset[0]
			count = 0
			
			for predio in queryset:
				aux = count
				count = 0
				
				for source in source_queryset:
					if source.predio == predio:
						count = count + 1
											
				if count < aux:
					smallest = predio
						
			return smallest

	def get_smallest_volume(self):
		queryset = self.object_list
		source_queryset = Nacimiento.objects.all()
		smallest = source_queryset[0]
		caudal = 0

		for predio in queryset:
			aux = caudal
			caudal = 0

			for source in source_queryset:
				if source.predio == predio:
					caudal = caudal+ source.caudal

			if caudal < aux:
				smallest = predio

		return smallest


		def get_smallest_pressure(self):
			
			smallest = self.object_list[0]

			for item in queryset:
				if item.presion_antropica > smallest.presion_antropica:
					smallest = item

			return smallest
############################################################3

		def get_highest_caudal_source(self):
			queryset = Nacimiento.objects.all()
			smallest = queryset[0]

			for item in queryset:
				if item.caudal < smallest.caudal:
					smallest = item

			return smallest


		def get_higher_caudal_source(self):
			queryset = Nacimiento.objects.all()
			highest = queryset[0]
			for item in queryset:
				if item > highest:
					highest = item
			return highest



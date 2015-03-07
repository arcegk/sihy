# -*- encoding: utf-8 -*-
from django.shortcuts import render
import json
from .models import Predio , Nacimiento
from endless_pagination.views import AjaxListView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.db.models import Max , Min

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
  		context['min_area'] = self.get_smallest_area()
  		context['min_source'] = self.get_smallest_source()
  		context['min_volume'] = self.get_smallest_volume()
  		

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
					'temperatura': item.temperatura_promedio,
					'via_pavimentada': item.via_pavimentada,
					'via_destapada': item.via_destapada,
					'via_trocha': item.via_trocha,
					'id' : item.id , 
					'nombre' : item.nombre ,
					'n_acta' : item.numero_acta,
					'f_acta' : item.fecha_acta,
					'observaciones' : item.observaciones,
					'url' : item.url,
					'ecosistema': item.ecosistema,
					'zona_de_vida': item.zona_de_vida,
					'altura_max': item.altura_max,
					'altura_min': item.altura_min,
					'clima': item.clima,
					'suelos': item.suelos,
					'relieve': item.relieve
					'clase_agrologica': item.clase_agrologica,
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
				'altura' : item.altura,
				'latitude' : item.latitude,
				'longitude' : item.longitude,
				'identificador' : item.identificador,
				
				})
		return json.dumps(items)

############################################################################
	def get_highest_area(self):

		arg = Predio.objects.all().aggregate(Max('area'))['area__max']
		result = Predio.objects.get(area=arg)
		return result.nombre + '-' + str(result.area)

	
	def get_highest_source(self):
		queryset = self.object_list
		source_queryset = Nacimiento.objects.all()
		highest = queryset[0]
		result = highest.nombre + "-" 
		count = 0
		aux = 0
		for predio in queryset:
			
			count = 0
			
			for source in source_queryset:
				if source.predio == predio:
					count = count + 1
										
			if count > aux:
				aux = count
				highest = predio
				result = highest.nombre + " - " + str(count) + " Nacimiento(s)" 				
		return result 

	def get_highest_volume(self):
		queryset = self.object_list
		source_queryset = Nacimiento.objects.all()
		highest = queryset[0]
		result = highest.nombre + " " 
		caudal = 0

		aux = source_queryset[0].caudal
		for predio in queryset:
			caudal = 0

			for source in source_queryset:
				if source.predio == predio:
					caudal = caudal+ source.caudal

			if caudal > aux:
				aux = caudal
				highest = predio
				result = highest.nombre + " - " + str(caudal) + "(L/s)"

		return result


#############################################################################
					
	def get_smallest_area(self):
		args = Predio.objects.all().aggregate(Min('area'))['area__min']
		result = Predio.objects.get(area=args)
		return result.nombre + '-' + str(result.area)

			
	def get_smallest_source(self):
			queryset = self.object_list
			source_queryset = Nacimiento.objects.all()
			smallest = queryset[0]
			result = smallest.nombre
			count = 0
			aux =  100
			for predio in queryset:
				
				count = 0
				
				for source in source_queryset:
					if source.predio == predio:
						count = count + 1
											
				if count < aux:
					aux = count
					smallest = predio
					result = smallest.nombre 
						
			return result + " - " + str(aux) + " Nacimiento(s)" 

	def get_smallest_volume(self):
		queryset = self.object_list
		source_queryset = Nacimiento.objects.all()
		smallest = queryset[0]
		result = smallest.nombre 
		caudal = 0
		aux = source_queryset[0].caudal
		for predio in queryset:
			
			caudal = 0

			for source in source_queryset:
				if source.predio == predio:
					caudal = caudal + source.caudal
			
			if caudal < aux:
				smallest = predio
				aux = caudal
				result = smallest.nombre + " - " + str(caudal) + '(L/s)'

		return result 



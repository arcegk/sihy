from django.shortcuts import render
import json
from .models import Predio , Nacimiento
from endless_pagination.views import AjaxListView
from django.views.generic.list import ListView
from django.core.paginator import Paginator


class MapView(ListView):
	template_name = 'map.html'
	queryset = Predio.objects.all()

	print queryset

	def get_context_data(self , **kwargs):
		context = super(MapView, self).get_context_data(**kwargs)
  		context['object_list_json'] = self.get_json_results()
  		context['json_object_list'] = self.get_json()
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
	                })

	        return json.dumps(items)

	def get_json(self):
		val = Nacimiento.objects.all()
		p = Paginator(val, 1)
		print p
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

"""class NacimientoListView(ListView):
	template_name = 'map.html'
	queryset = Nacimiento.objects.all()

	def get_context_data(self , **kwargs):
		context = super(NacimientoListView, self).get_context_data(**kwargs)
		context['json_object_list'] = self.get_json_results()
		return context

	def get_json_results(self):

		items = []
		for item in self.object_list:
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
				'cabecera_municipal' : item.cabecera_municipal, 
				'topo_especificacion' : item.topo_especificacion,
				'altura' : item.altura,
				'predio' : item.predio,
				'latitude' : item.latitude,
				'longitude' : item.longitude,
				})
		return json.dumps(items)
"""
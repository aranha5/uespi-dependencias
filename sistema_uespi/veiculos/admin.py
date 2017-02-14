from django.contrib import admin

from .models import Veiculos

class VeiculosSet(admin.ModelAdmin):
	fieldsets = [
		('Informações dos veículos', {'fields': ['marca_modelo', 'tipo_veiculo','placa','data_revisao','estado', 'cidade', 'chassi', 'cor', 'situacao']}),
	]

	list_display = ('marca_modelo', 'tipo_veiculo','placa', 'situacao')
	

admin.site.register(Veiculos, VeiculosSet)
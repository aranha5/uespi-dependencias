from django.contrib import admin

from .models import Equipamentos

class EquipamentosSet(admin.ModelAdmin):
	fieldsets = [
		('Informações do equipamento', {'fields': ['codigo', 'nome', 'modelo', 'estado_fisico', 'data_aquisicao', 'obeservacao']}),
	]

	list_display = ('nome', 'estado_fisico', 'obeservacao')
	

admin.site.register(Equipamentos, EquipamentosSet)
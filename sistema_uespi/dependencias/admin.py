from django.contrib import admin

from .models import Dependencia

class DependenciasSet(admin.ModelAdmin):
	fieldsets = [
		('Informações da dependeência', {'fields': ['nome_dependencia','identificacao','area','situacao']}),
	]

	list_display = ('nome_dependencia', 'identificacao', 'situacao', 'data_inclusao')
	

admin.site.register(Dependencia, DependenciasSet)
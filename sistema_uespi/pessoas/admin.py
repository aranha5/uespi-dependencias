from django.contrib import admin

from .models import User, PessoaFisica, PessoaJuridica

class PF(admin.StackedInline):
	model = PessoaFisica
	extra = 0
	max_num = 1

class PJ(admin.StackedInline):
	model = PessoaJuridica
	extra = 0
	max_num = 1

class UserSet(admin.ModelAdmin):
	inlines  = [PF,PJ]
	fieldsets = [
		('Informações de Login', {'fields': ['username','password','email','groups']}),
	]

	list_display = ('username', 'email')

admin.site.register(User, UserSet)
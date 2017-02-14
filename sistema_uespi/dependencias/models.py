from django.db import models

class Dependencia(models.Model):
	nome_dependencia = models.CharField('Nome da dependência', max_length=60)
	identificacao = models.CharField('Identificação da dependência', max_length=14)
	area = models.CharField(max_length=4)
	situacao = models.CharField(max_length=60)
	data_inclusao = models.DateField(auto_now_add=True)
from django.db import models

class Equipamentos(models.Model):

	SITUATION_CHOICE = (
		('D', 'Disponível'),
		('R', 'Reservado'),
		('E', 'Em manutenção'),
	)

	codigo = models.CharField('Código do equipamento', max_length=100, unique=True)
	nome = models.CharField('Nome do equipamento', max_length=30)
	modelo = models.CharField('Modelo', max_length=100)
	estado_fisico =  models.CharField(max_length=2, choices=SITUATION_CHOICE, blank=True)
	data_aquisicao = models.DateField('Data da ultima revisão (DD/MM/YYYY)', auto_now_add=False)
	obeservacao = models.TextField('Obersações sobre o equipamento', max_length=100)
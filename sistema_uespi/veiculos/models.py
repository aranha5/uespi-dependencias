from django.db import models

class Veiculos(models.Model):

	TYPE_CHOICE = (
		('O', 'Ônibus'),
		('M', 'Microônibus'),
		('C', 'Carro')
	)

	UF_CHOICE = (
	    ('AC', 'Acre'), 
	    ('AL', 'Alagoas'),
	    ('AP', 'Amapá'),
	    ('BA', 'Bahia'),
	    ('CE', 'Ceará'),
	    ('DF', 'Distrito Federal'),
	    ('ES', 'Espírito Santo'),
	    ('GO', 'Goiás'),
	    ('MA', 'Maranão'),
	    ('MG', 'Minas Gerais'),
	    ('MS', 'Mato Grosso do Sul'),
	    ('MT', 'Mato Grosso'),
	    ('PA', 'Pará'),
	    ('PB', 'Paraíba'),
	    ('PE', 'Pernanbuco'),
	    ('PI', 'Piauí'),
	    ('PR', 'Paraná'),
	    ('RJ', 'Rio de Janeiro'),
	    ('RN', 'Rio Grande do Norte'),
	    ('RO', 'Rondônia'),
	    ('RR', 'Roraima'),
	    ('RS', 'Rio Grande do Sul'),
	    ('SC', 'Santa Catarina'),
	    ('SE', 'Sergipe'),
	    ('SP', 'São Paulo'),
	    ('TO', 'Tocantins')
	)

	SITUATION_CHOICE = (
		('D', 'Disponível'),
		('R', 'Reservado'),
		('E', 'Em manutenção'),
		('A', 'Alugado')
	)

	marca_modelo = models.CharField('Marca/Modelo', max_length=20)
	tipo_veiculo = models.CharField(max_length=2, choices=TYPE_CHOICE, blank=True)
	placa = models.CharField('Placa do veículo', max_length=8)
	data_revisao = models.DateField('Data da ultima revisão (DD/MM/YYYY)', auto_now_add=False)
	estado = models.CharField(max_length=2, choices=UF_CHOICE , blank=True)
	cidade = models.CharField('Cidade', max_length=20)
	chassi = models.CharField('Chassi', max_length=18)
	cor = models.CharField('Cor', max_length=11)
	situacao = models.CharField(max_length=2, choices=SITUATION_CHOICE, blank=True)
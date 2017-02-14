from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
	UserManager)

class User(AbstractBaseUser,PermissionsMixin):
	username = models.CharField('Usuário', max_length=20, unique=True)
	email = models.EmailField('E-mail')

	is_active = models.BooleanField(
		'Está Ativo?',
		blank=True,
		default=True
	)
	is_staff = models.BooleanField(
		'Administrador', 
		blank=True, 
		default=True
	)
	date_joined = models.DateTimeField(
		'Data de Cadastro', 
		auto_now_add=True
	)
	
	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

class PessoaFisica(models.Model):
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

	GENDER_CHOICE = (
		('M', 'Masculino'),
		('F', 'Feminino')
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cpf = models.CharField('CPF', max_length=11, unique=True)

	name = models.CharField('Nome', max_length=50)
	sexo = models.CharField(max_length=2, choices=GENDER_CHOICE, blank=True)
	endereco = models.CharField('Endereço', max_length=50)
	cidade = models.CharField('Cidade', max_length=20)
	estado = models.CharField(max_length=2, choices=UF_CHOICE)
	cep = models.CharField('CEP', max_length=8, null=True)


	
class PessoaJuridica(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cnpj = models.CharField(max_length=12, unique=True)
	razao_social = models.CharField(max_length=50, null=True)
	nome_fantasia = models.CharField(max_length=20, null=True)

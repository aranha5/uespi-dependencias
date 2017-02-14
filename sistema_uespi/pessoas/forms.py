from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import get_user_model
from localflavor.br.forms import BRCPFField, BRCNPJField

from .models import User, PessoaFisica, PessoaJuridica

User = get_user_model()

class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				'Senhas não são iguais'
			)
		return password2

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class RegisterPessoaFisica(forms.ModelForm):
	cpf = BRCPFField(required=True)

	class Meta:
		model = PessoaFisica
		fields = '__all__'
		#exclude = ['user']
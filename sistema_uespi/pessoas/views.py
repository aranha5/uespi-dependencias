from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import User, PessoaFisica
from .forms import RegisterForm, RegisterPessoaFisica

def new_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect(reverse('pessoas:pessoa_fisica', args=(new_user.id,)))
	else:
		form = RegisterForm()
	return render(request, 'pessoas/new_user.html', {'form':form})

def pessoa_fisica(request, pk):
	user = User.objects.get(id=pk)
	PFisicaInlineFormSet = inlineformset_factory(User,PessoaFisica, exclude=['user'] ,extra=1, can_delete=False)
	if request.method == 'POST':
		form = PFisicaInlineFormSet(request.POST, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Usuário cadastrado com sucesso!')
			return HttpResponseRedirect(reverse('home'))
	else:
		form = PFisicaInlineFormSet(instance=user)
	return render(request, 'pessoas/pessoa_fisica.html', {'form':form})
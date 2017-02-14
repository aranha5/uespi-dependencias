from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', login, {'template_name': 'index.html'}, name='home'),
    url(r'^novo_usuario/', include('sistema_uespi.pessoas.urls', namespace='pessoas')),	
    url(r'^admin/', admin.site.urls, name='admin'),
]


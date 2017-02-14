from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.new_user, name='novo_usuario'),
	url(r'^(?P<pk>[0-9]+)/', views.pessoa_fisica, name='pessoa_fisica'),
]



from django.conf.urls import patterns, url

from apps.solisitudes import views

urlpatterns = [
	url(r'^$', views.solisitud_list, name='index'),
	url(r'^nueva$', views.solisitud_create, name='nueva_solisitud'),
	url(r'^editar/(?P<pk>\d+)$', views.solisitud_update, name='editar_solisitud'),
	url(r'^borrar/(?P<pk>\d+)$', views.solisitud_delete, name='borrar_solisitud'),
	
]
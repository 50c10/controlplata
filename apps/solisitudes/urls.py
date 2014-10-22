from django.conf.urls import url

from apps.solisitudes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_solisitudes/$',views.list_solisitud, name='lista_solisitudes'),
]
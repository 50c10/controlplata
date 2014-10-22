from django.shortcuts import render
from django.http import HttpResponse


from apps.solisitudes.models import Solisitud
# Create your views here.

def index(request):
    return render(request, 'solisitudes/solisitud.html')

def list_solisitud(request):
	solisitudes_list = Solisitud.objects.all()
	context = {'lista_solisitudes': solisitudes_list}
	return render(request, 'solisitudes/solisitud_list.html',context)
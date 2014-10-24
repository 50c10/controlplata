from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from apps.solisitudes.models import Solisitud
# Create your views here.

class SolisitudForm(ModelForm):
    class Meta:
        model = Solisitud

def solisitud_list(request, template_name='solisitudes/solisitud_list.html'):
    solisitudes = Solisitud.objects.all()
    data = {}
    data['object_list'] = solisitudes
    return render(request, template_name, data)

def solisitud_create(request, template_name='solisitudes/nuevo.html'):
    form = SolisitudForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def solisitud_update(request, pk, template_name='solisitudes/nuevo.html'):
    solisitud = get_object_or_404(Solisitud, pk=pk)
    form = SolisitudForm(request.POST or None, instance=solisitud)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def solisitud_delete(request, pk, template_name='solisitudes/solisitud_borrar.html'):
    solisitud = get_object_or_404(Solisitud, pk=pk)    
    if request.method=='POST':
        solisitud.delete()
        return redirect('index')
    return render(request, template_name, {'object':solisitud})
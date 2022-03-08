from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps_rh.departamento.models import Departamento


@login_required()
def Home(request):
    data = {}
    data['usuario'] = request.user
    return  render( request, "core/index.html",data)

def departamentos_ajax(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos})


def filtra_funcionarios(request):
    depart = request.GET['outro_param']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')
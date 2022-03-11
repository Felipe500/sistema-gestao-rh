from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps_rh.core.serializers import UserSerializer, GroupSerializer
from .tasks import send_relatorio

from apps_rh.departamento.models import Departamento


@login_required()
def Home(request):
    data = {}
    data['usuario'] = request.user
    return  render( request, "core/index.html",data)

def departamentos_ajax(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def celery(request):
    send_relatorio.delay()
    return HttpResponse('Tarefa incluida na fila para execucao')

def filtra_funcionarios(request):
    depart = request.GET['outro_param']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')
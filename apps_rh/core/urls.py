from django.urls import path, include
from .views import Home, filtra_funcionarios, departamentos_ajax,celery

urlpatterns = [
    path('', Home, name='home'),
    path('departamentos-ajax/', departamentos_ajax, name='departamentos_ajax'),
    path('filtra-funcionarios/', filtra_funcionarios, name='filtra_funcionarios'),
    path('celery/', celery, name='celery'),
]



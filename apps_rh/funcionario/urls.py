
from django.urls import path, include
from .views import (FuncionariosList,
                    FuncionarioUpdate,
                    FuncionarioDelete,FuncionarioCreate)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='deletar_funcionario'),
    path('Novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
]

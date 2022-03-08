from django.urls import path
from .views import (FuncionariosList,
                    FuncionarioUpdate,
                    FuncionarioDelete,
                    FuncionarioCreate,
                    relatorio_funcionarios,
                    Pdf,
                    PdfDebug)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='deletar_funcionario'),
    path('Novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('relatorio_funcionarios', relatorio_funcionarios, name='relatorio_funcionarios'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
    path('relatorio_funcionarios_html_debug', PdfDebug.as_view(), name='relatorio_funcionarios_html_debug'),
]

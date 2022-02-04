from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('funcionarios/', include('apps_rh.funcionario.urls')),
    path('', include('apps_rh.core.urls')),

    path('departamentos/', include('apps_rh.departamento.urls')),
    path('empresa/', include('apps_rh.empresa.urls')),
    path('documento/', include('apps_rh.documentos.urls')),
    path('horas-extras/', include('apps_rh.registro_hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from apps_rh.funcionario.api.views import FuncionarioViewSet
from apps_rh.registro_hora_extra.api.views import RegistroHoraExtraViewSet
from rest_framework import routers
from apps_rh.core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/banco-horas', RegistroHoraExtraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('funcionarios/', include('apps_rh.funcionario.urls')),
    path('', include('apps_rh.core.urls')),

    path('departamentos/', include('apps_rh.departamento.urls')),
    path('empresa/', include('apps_rh.empresa.urls')),
    path('documento/', include('apps_rh.documentos.urls')),
    path('horas-extras/', include('apps_rh.registro_hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

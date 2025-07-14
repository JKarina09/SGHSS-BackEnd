from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, ConsultaViewSet, ProfissionalViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'profissionais', ProfissionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, ConsultaViewSet, ProfissionalViewSet, login_view

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'profissionais', ProfissionalViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('api/', include(router.urls)),
]
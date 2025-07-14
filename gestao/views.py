from rest_framework import viewsets
from .models import Paciente, Consulta, ProfissionalSaude
from .serializers import PacienteSerializer, ConsultaSerializer, ProfissionalSaudeSerializer

# Create your views here.

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer    

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

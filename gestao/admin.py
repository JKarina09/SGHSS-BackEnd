from django.contrib import admin
from .models import Usuario, Paciente, ProfissionalSaude, Consulta, Pronturario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(ProfissionalSaude)
admin.site.register(Consulta)
admin.site.register(Pronturario)

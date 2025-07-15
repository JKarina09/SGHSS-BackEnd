from django.contrib import admin
from .models import Usuario, Paciente, ProfissionalSaude, Consulta, Pronturario

# Register your models here.

#Titulos personalizados do Admin

admin.site.site_header = 'SGHSS - Administração'
admin.site.site_title = "SGHSS"
admin.site.index_title = "Painel de Gerenciamento"

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'perfil', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('perfil',)
   

@admin.register(Paciente)    
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cpf', 'data_nascimento', 'telefone')
    search_fields = ('usuario__username', 'cpf')
    list_filter = ('data_nascimento',)

@admin.register(ProfissionalSaude)
class ProfissionalSaudeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'crm', 'especialidade')
    search_fields = ('usuario__username', 'crm')
    list_filter = ('especialidade',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional', 'data', 'hora', 'status')
    search_fields = ('paciente__usuario__username', 'profissional__usuario__username')
    list_filter = ('data', 'status')   

@admin.register(Pronturario)
class PronturarioAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'observacao', 'receita')
    search_fields = ('consulta__paciente__usuario__username',)         


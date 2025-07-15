from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Modelo Usuario (herda de AbstractUser para login)
class Usuario(AbstractUser):
    PERFIL_CHOICES = [
        ('admin', 'administrador'),
        ('profissional', 'Profissional de Saúde'),
        ('paciente', 'Paciente'),
    ]

    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)

    def __str__(self):
        return f'{self.username} ({self.perfil})'
    
class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario.get_full_name()
    
class ProfissionalSaude(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    crm = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario.get_full_name()} - {self.especialidade}'
    
    class Meta:
        verbose_name_plural = "Profissionais de Saúde"

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('concluída', 'Concluída'),
        ('cancelada', 'Cancelada'),
        ('reagendada', 'Reagendada')
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendada')  

    def __str__(self):
        return f'Consulta em {self.data} ás {self.hora} com {self.profissional}'


class Pronturario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    observacao = models.TextField()
    receita = models.TextField(blank=True)

    def __str__(self):
        return f'Prontuário da Consulta {self.consulta.id}'       

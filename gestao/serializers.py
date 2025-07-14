from rest_framework import serializers
from .models import Usuario, Paciente, Consulta, ProfissionalSaude

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'perfil', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'validators':[]}}
        

    def create (self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        # Atualiza os campos, exceto a senha
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.perfil = validated_data.get('perfil', instance.perfil)
        
        # Atualiza a senha se fornecida
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance 
        
class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Paciente
        fields = ['id', 'usuario', 'cpf', 'data_nascimento', 'telefone']
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data)
        paciente = Paciente.objects.create(usuario=usuario, **validated_data)
        return paciente             
    

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = instance.usuario

        usuario.username = usuario_data.get('username', usuario.username)
        usuario.email = usuario_data.get('email', usuario.email)
        usuario.perfil = usuario_data.get('perfil', usuario.perfil)

        if 'password' in usuario_data:
            usuario.set_password(usuario_data['password'])

        usuario.save()

        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.save()

        return instance
    
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'paciente', 'profissional', 'data', 'hora', 'status']    


class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = ProfissionalSaude
        fields = ['id', 'usuario', 'crm', 'especialidade']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data)
        return ProfissionalSaude.objects.create(usuario=usuario, **validated_data)      
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # La contraseña solo se puede escribir y debe pasar las validaciones de seguridad de Django
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # Opcional:
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # Definimos todos los campos que el frontend puede enviar al registrar
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone']

    # Lógica que se ejecuta al llamar a serializer.save()
    def create(self, validated_data):
        # Usamos create_user para garantizar que la contraseña se guarde con hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            # Usamos .get() con valor por defecto '' para campos opcionales
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone=validated_data.get('phone', '')
        )
        return user

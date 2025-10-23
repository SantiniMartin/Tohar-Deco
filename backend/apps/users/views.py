from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny 

from .serializers import RegisterSerializer # Importamos tu serializador

# Vista para manejar las peticiones de Registro
class RegistrationView(APIView):
    # Permite el acceso sin autenticación (ya que el usuario se está creando)
    permission_classes = [AllowAny] 
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            # Llama al método create() del serializador
            user = serializer.save() 
            
            return Response(
                {
                    "message": "Registro exitoso.",
                    "user_id": user.id,
                    "email": user.email
                }, 
                status=status.HTTP_201_CREATED
            )
        
        # Devuelve errores de validación (ej: contraseña débil, email repetido)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

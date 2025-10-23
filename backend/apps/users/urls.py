from django.urls import path
# La vista de Login (JWT) y la vista de Registro
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView

urlpatterns = [
    #ENDPOINT DE REGISTRO
    # URL final: /api/auth/register/
    path('register/', RegistrationView.as_view(), name='user_register'), 
    
    #ENDPOINT DE LOGIN (Obtener tokens)
    # URL final: /api/auth/token/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    #ENDPOINT para renovar el token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

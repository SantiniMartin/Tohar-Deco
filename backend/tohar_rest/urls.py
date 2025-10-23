# tohar_rest/urls.py
from django.urls import include, path
from apps.users.admin import open_admin_site  # tu admin abierto

urlpatterns = [
    #path('', home), DEFINIR PATH DE INCIO PLS
    path('admin/', open_admin_site.urls),          # usa tu admin abierto
    path('api/users/', include('apps.users.urls')),  # ruta correcta a tu app
]

from django.urls import include, path
from apps.users.admin import open_admin_site  
from .views import api_home


urlpatterns = [
    path('', api_home),
    path('admin/', open_admin_site.urls),          
    path('api/auth/', include('apps.users.urls')),
]

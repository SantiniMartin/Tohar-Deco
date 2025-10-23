from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.admin import AdminSite

User = get_user_model()

class OpenAdminSite(AdminSite):
    site_header = "Panel de Administración"
    site_title = "Admin"
    index_title = "Bienvenido al Admin"

    def has_permission(self, request):
        # Permite el acceso si el usuario está autenticado
        return request.user.is_authenticated

open_admin_site = OpenAdminSite(name='open_admin')

@admin.register(User, site=open_admin_site)
class CustomUserAdmin(UserAdmin):
    #  Agregar 'phone' a la lista de columnas
    list_display = UserAdmin.list_display + ('phone',)
    
    #  Agregar 'phone' a los campos editables del formulario
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('phone',)}),
    )

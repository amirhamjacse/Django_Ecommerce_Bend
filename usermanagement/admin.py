from django.contrib import admin
from .models import Role, User

# Register the Role model
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',) 
    list_filter = ('name',) 


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'role', 'status', 'phone_number', 'company_id', 'otp_expired_at', )
    search_fields = ('username', 'email')
    list_filter = ('role', 'status')


admin.site.register(User, UserAdmin)

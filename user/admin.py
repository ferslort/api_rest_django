from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal Info', {'fields': ('first_name', 'last_name')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

  )

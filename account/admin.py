from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CustomUserCreationForm, CustomUserChangeForm
from account.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('phone', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('phone', 'iin')

    fieldsets = (
        (
            'Main', {
                'fields': ('phone', 'password',)
            }
        ),
        (
            'Additional information', {
                'fields': ('first_name', 'last_name', 'iin', 'email', 'role')
            }
        ),
        (
            'Permissions', {
                'fields': ('is_staff', 'is_active', )  # 'user_permissions')
            }
        )
    )
    add_fieldsets = (
        (
            'Main', {
                'classes': ('wide',),
                'fields': ('phone', 'email', 'iin', 'role', 'password1', 'password2',)
            }
        ), (
            'Permissions', {
                'fields': ('is_staff', 'is_active')
            }
        )
    )
    search_fields = ('phone', 'email', 'iin')
    ordering = ('phone', 'email', 'iin')




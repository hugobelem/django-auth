from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'username', 'email', 'phone']
    search_fields = ['first_name__startswith']
    readonly_fields = ['date_joined', 'last_login']

    def get_form(self, request, obj, **kwargs) -> Any:
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['is_superuser'].disabled = True

        return form

admin.site.register(CustomUser, CustomUserAdmin)

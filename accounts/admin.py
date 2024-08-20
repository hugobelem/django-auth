from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'username', 'email', 'phone']
    search_fields = ['first_name__startswith']
    readonly_fields = ['date_joined', 'last_login']

    def get_readonly_fields(self, request, obj=None):
        # Make all fields read-only for non-superusers
        if not request.user.is_superuser:
            readonly_fields = list(
                set([field.name for field in self.opts.local_fields] +
                    [field.name for field in self.opts.local_many_to_many])
            )

            # Remove list of fields from readonly fields if needed
            fields = ['is_submitted']
            for field in fields:
                if field in readonly_fields:
                    readonly_fields.remove(field)

            return readonly_fields

        # Read-only fields for superusers
        return ['date_joined', 'last_login']

admin.site.register(CustomUser, CustomUserAdmin)

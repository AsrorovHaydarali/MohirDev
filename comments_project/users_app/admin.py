from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "photo",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "photo",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)

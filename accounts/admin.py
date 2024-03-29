from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('age',)}),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", )}),
    )
    list_display = ['username', 'age', 'email', 'is_staff']


admin.site.register(CustomUserModel, CustomUserAdmin)

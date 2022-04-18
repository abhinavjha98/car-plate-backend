from django.contrib import admin
from .models import CustomUser
# Register your models here.
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User details",{
                'fields':(
                    'name',
                    'dob',
                    'profession',
                    'user_id'
        )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from petstagram_two.accounts.forms import AppUserChangeForm
from petstagram_two.accounts.models import AppUser

UserModel = get_user_model()

# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    model = UserModel
    add_form = UserCreationForm
    form = AppUserChangeForm
    list_display = ['pk', 'email', 'is_staff', 'is_superuser', ]
    search_fields = ['email',]
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('important dates', {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )
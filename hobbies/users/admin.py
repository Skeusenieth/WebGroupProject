from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from user_hobbies.models import Hobby


class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'name', 'date_of_birth', 'is_staff', 'is_superuser')
    # Fields to filter by in the admin
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    # Fields to search in the admin
    search_fields = ('username', 'email', 'name')

    # Customize the user form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'date_of_birth', 'hobbies')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'date_of_birth', 'hobbies')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the list view
    search_fields = ('name',)  # Fields to enable search
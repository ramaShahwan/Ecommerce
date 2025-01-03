from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Customer

# Unregister the default Group model
admin.site.unregister(Group)

# Customizing the User Admin
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'phone', 'gender', 'is_superuser', 'is_active')
    list_filter = ('is_active', 'is_superuser', 'gender')
    
    actions = None
    fieldsets = (
        (None, {'fields': ('username', 'password', 'last_login', 'date_joined')}),
        (('Personal info'), {
            'fields': (
                'email',
                'phone',
                'gender',
                'profile_image'
            )
        }),
        (('Permissions'), {
            'fields': ('is_active', 'is_superuser'),
        })
    )
    
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')

# Customizing the Customer Admin
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'father_name', 'last_name', 'birth_date', 'user')
    search_fields = ('first_name', 'father_name', 'last_name', 'user__username')
    ordering = ('last_name', 'first_name')

# Registering the User model with the custom UserAdmin
admin.site.register(User, CustomUserAdmin)

# Registering the Customer model with the custom CustomerAdmin
admin.site.register(Customer, CustomerAdmin)

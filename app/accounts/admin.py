from django.contrib import admin

# Register your models here.
from .models import User
#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'rut')
    list_filter = ('is_active',)

admin.site.register(User, UserAdmin)
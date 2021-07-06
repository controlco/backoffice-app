from django.contrib import admin
from .models import User, Report


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'rut')
    list_filter = ('is_active',)
    readonly_fields = ['password']

    def has_add_permission(self, request, obj=None):
        return False

     

admin.site.register(User, UserAdmin)
admin.site.register(Report)

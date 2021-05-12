from django.contrib import admin

# Register your models here.
from .models import Property
#admin.site.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'surface', 'price', 'is_active')
    list_filter = ('is_active',)

admin.site.register(Property, PropertyAdmin)
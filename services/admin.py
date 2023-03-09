from django.contrib import admin
from .models import Service


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'created_at', 'modified_at')
    search_fields = ['name']


admin.site.register(Service, ServicesAdmin)


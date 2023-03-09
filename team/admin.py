from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'description', 'created_at']
    search_fields = ['fname']


admin.site.register(Team, TeamAdmin)

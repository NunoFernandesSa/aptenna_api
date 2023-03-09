from django.contrib import admin

from skills.models import Skill


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Skill, SkillsAdmin)

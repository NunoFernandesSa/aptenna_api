from django.contrib import admin

from jobs.models import Job


class JobsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Job, JobsAdmin)

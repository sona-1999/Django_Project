from django.contrib import admin
from . models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','user','completed')
    search_fields = ('title', )
    list_filter = ('completed', )


admin.site.register(Task, TaskAdmin)

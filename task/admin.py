from django.contrib import admin
from task.models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'created_at', 'project_id']

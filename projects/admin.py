from django.contrib import admin
from projects.models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug',
                    'created_at', 'updated_at', 'user', 'dateDelivery', 'isCompleted']

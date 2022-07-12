from django.db import models
from user.models import User
from django.db.models import SET_NULL, CASCADE


class Task(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=False)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField(default=False)
    priority = models.IntegerField(default=0, null=False)
    dateDelivery = models.DateField(null=True)
    project = models.ForeignKey(
        to='projects.Project', on_delete=CASCADE, null=False, related_name='tasks')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

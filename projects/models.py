from django.db import models
from user.models import User
from django.db.models import SET_NULL


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    dateDelivery = models.DateField(null=True)
    description = models.TextField(blank=True)
    is_disabled = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

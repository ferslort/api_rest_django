from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'slug', 'description', 'created_at',
                  'isCompleted', 'project', 'priority', 'dateDelivery')

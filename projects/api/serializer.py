from rest_framework import serializers
from projects.models import Project
from task.api.serializer import TaskSerializer


class ProjectRegistersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'description',
                  'created_at', 'is_disabled', 'user', 'dateDelivery', 'isCompleted']


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'slug', 'description',
                  'is_disabled', 'dateDelivery', 'isCompleted', 'user', 'tasks')
